from kfp import dsl
from kfp.dsl import component, Output, Dataset

@component(base_image="python:3.9")
def collect_filtered_logs(
    output_report: Output[Dataset],
    log_keywords: str = "crash,error,fail,oomkilled,evicted",
    event_keywords: str = "CrashLoopBackOff,Failed,Unhealthy,Evicted,OOME"
):
    import subprocess
    import os
    import json
    from datetime import datetime
    from collections import defaultdict

    tmp_report_path = "/tmp/report.html"
    tmp_css_path = "/tmp/report.css"
    excluded_namespace = "kubeflow-user-example-com"

    # GitHub raw URL 변환 (CSS)
    css_url = "https://raw.githubusercontent.com/Rosa1026/Kubeflow/report/html/style.css"

    # 필수 도구 설치 및 kubectl 준비
    subprocess.run(["apt-get", "update", "-y"], check=True)
    subprocess.run(["apt-get", "install", "-y", "procps", "curl"], check=True)
    subprocess.run([
        "curl", "-LO", "https://storage.googleapis.com/kubernetes-release/release/v1.24.0/bin/linux/amd64/kubectl"
    ], check=True)
    subprocess.run(["chmod", "+x", "kubectl"], check=True)
    subprocess.run(["mv", "kubectl", "/usr/local/bin/"], check=True)

    # CSS 파일 다운로드
    subprocess.run(["curl", "-sSL", "-o", tmp_css_path, css_url], check=True)

    # 키워드 리스트로 분리, 소문자 변환
    log_kw_list = [k.strip().lower() for k in log_keywords.split(",") if k.strip()]
    event_kw_list = [k.strip().lower() for k in event_keywords.split(",") if k.strip()]

    seen_namespaces = set()
    namespace_events = {}
    status_counts = defaultdict(int)
    high_usage_pods = []

    def get_status_color(status):
        return {
            "running": "green",
            "crashloopbackoff": "red",
            "failed": "red",
            "error": "red",
            "pending": "orange",
            "succeeded": "blue"
        }.get(status.lower(), "gray")

    def parse_resource_quantity(q):
        try:
            if q.endswith("m"):
                return float(q[:-1]) / 1000.0
            elif q.endswith("Mi"):
                return float(q[:-2])
            elif q.endswith("Gi"):
                return float(q[:-2]) * 1024
            else:
                return float(q)
        except Exception:
            return 0

    def get_resource_usage_percentage(used, limit):
        if limit == 0:
            return "N/A"
        usage_percentage = (used / limit) * 100
        if usage_percentage > 1000:
            return "N/A"
        return round(usage_percentage, 1)

    # Pod metrics 수집
    top_pods = subprocess.getoutput("kubectl top pod --all-namespaces --no-headers").splitlines()
    pod_metrics = {}
    for line in top_pods:
        parts = line.split()
        if len(parts) >= 4:
            namespace, name, cpu, mem = parts[:4]
            pod_metrics[(namespace, name)] = {
                "cpu": parse_resource_quantity(cpu),
                "memory": parse_resource_quantity(mem)
            }

    # Pod 사양과 리소스 사용량 비교
    pod_specs = json.loads(subprocess.getoutput("kubectl get pods --all-namespaces -o json"))
    for item in pod_specs["items"]:
        ns = item["metadata"]["namespace"]
        if ns == excluded_namespace:
            continue
        name = item["metadata"]["name"]
        containers = item["spec"].get("containers", [])
        for container in containers:
            res = container.get("resources", {})
            req = res.get("requests", {})
            req_cpu = parse_resource_quantity(req.get("cpu", "0")) if "cpu" in req else 0
            req_mem = parse_resource_quantity(req.get("memory", "0")) if "memory" in req else 0
            usage = pod_metrics.get((ns, name), {})
            used_cpu = usage.get("cpu", 0)
            used_mem = usage.get("memory", 0)

            cpu_usage_percent = get_resource_usage_percentage(used_cpu, req_cpu)
            mem_usage_percent = get_resource_usage_percentage(used_mem, req_mem)

            if cpu_usage_percent != "N/A" and cpu_usage_percent > 80:
                high_usage_pods.append({
                    "namespace": ns,
                    "name": name,
                    "cpu_ratio": cpu_usage_percent,
                    "mem_ratio": mem_usage_percent,
                    "used_cpu": used_cpu,
                    "used_mem": used_mem,
                    "req_cpu": req_cpu,
                    "req_mem": req_mem
                })

    # Pod 상태 수집
    pods_output = subprocess.getoutput(
        "kubectl get pods --all-namespaces -o custom-columns='NAMESPACE:.metadata.namespace,NAME:.metadata.name,STATUS:.status.phase' --no-headers"
    )
    pod_lines = pods_output.strip().split("\n")

    # 상태별 카운트 계산
    for line in pod_lines:
        if not line.strip():
            continue
        try:
            namespace, pod_name, status = line.split()
        except ValueError:
            continue
        if namespace == excluded_namespace:
            continue
        status_counts[status] += 1

    with open(tmp_report_path, "w") as f:
        f.write(f"""\
<html>
<head>
<meta charset="UTF-8">
<title>Kubernetes Cluster Health Report</title>
<style>
/* CSS 인라인 포함 (중괄호 이스케이프) */
{{
    background-color: #f9f9f9;
    font-family: Arial, sans-serif;
    padding: 10px;
}}
.keyword {{
    color: red;
    font-weight: bold;
}}
table {{
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 20px;
}}
th, td {{
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
}}
th {{
    background-color: #eee;
    cursor: pointer;
}}
tr:nth-child(even) {{
    background-color: #f2f2f2;
}}
tr:hover {{
    background-color: #ddd;
}}
</style>
<script>
// 테이블 정렬 기능 (간단 구현)
function sortTable(tableId, colIndex) {{
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById(tableId);
    switching = true;
    dir = "asc";
    while (switching) {{
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {{
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[colIndex];
            y = rows[i + 1].getElementsByTagName("TD")[colIndex];
            if (dir == "asc") {{
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {{
                    shouldSwitch = true;
                    break;
                }}
            }} else if (dir == "desc") {{
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {{
                    shouldSwitch = true;
                    break;
                }}
            }}
        }}
        if (shouldSwitch) {{
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount ++;
        }} else {{
            if (switchcount == 0 && dir == "asc") {{
                dir = "desc";
                switching = true;
            }}
        }}
    }}
}}
</script>
</head>
<body>
<h1>Kubernetes Cluster Health Report</h1>
""")

        # High usage pods 섹션
        f.write("<section><h2>⚠️ High Resource Usage Pods</h2>")
        if high_usage_pods:
            f.write('<table id="high_usage_pods"><thead><tr><th onclick="sortTable(\'high_usage_pods\', 0)">Namespace</th><th onclick="sortTable(\'high_usage_pods\', 1)">Name</th><th onclick="sortTable(\'high_usage_pods\', 2)">CPU Usage (%)</th><th onclick="sortTable(\'high_usage_pods\', 3)">Memory Usage (%)</th></tr></thead><tbody>')
            for p in high_usage_pods:
                f.write(f"<tr><td>{p['namespace']}</td><td>{p['name']}</td>"
                        f"<td style='color:red'>{p['cpu_ratio']}</td><td style='color:red'>{p['mem_ratio']}</td></tr>")
            f.write("</tbody></table>")
        else:
            f.write("<p>No high usage pods found.</p>")
        f.write("</section>")

        # Node metrics
        top_nodes = subprocess.getoutput("kubectl top node --no-headers").strip().splitlines()
        f.write("<section><h2>Node Resource Usage</h2><pre>")
        if top_nodes:
            f.write("NAME\tCPU\tCPU%\tMEM\tMEM%\n")
            for line in top_nodes:
                f.write(line + "\n")
        else:
            f.write("No node metrics available.\n")
        f.write("</pre></section>")

        # Pod 상태 요약
        f.write("<section><h2>Pod Status Summary</h2><ul>")
        for status, count in status_counts.items():
            f.write(f"<li>{status}: {count}</li>")
        f.write("</ul></section>")

        # Pod logs 및 describe, 이벤트 처리
        for line in pod_lines:
            if not line.strip():
                continue
            try:
                namespace, pod_name, status = line.split()
            except ValueError:
                continue
            if namespace == excluded_namespace:
                continue

            describe = subprocess.getoutput(f"kubectl describe pod {pod_name} -n {namespace}")
            logs = subprocess.getoutput(f"kubectl logs {pod_name} -n {namespace}")

            matched_describe_lines = [l for l in describe.splitlines() if any(k in l.lower() for k in log_kw_list)]
            matched_log_lines = [l for l in logs.splitlines() if any(k in l.lower() for k in log_kw_list)][-10:]
            matched_keywords = {kw for l in matched_describe_lines + matched_log_lines for kw in log_kw_list if kw in l.lower()}
            status_color = get_status_color(status)

            if matched_describe_lines or matched_log_lines:
                f.write(f"<section><h2>Pod: {pod_name} (Namespace: {namespace}) - "
                        f"<span style='color:{status_color};'>Status: {status}</span> - "
                        f"Keywords: {', '.join(matched_keywords)}</h2>")
                if matched_describe_lines:
                    f.write("<h3>Describe Output</h3><pre>")
                    for l in matched_describe_lines:
                        for kw in log_kw_list:
                            if kw in l.lower():
                                l = l.replace(kw, f"<span class='keyword'>{kw}</span>")
                        f.write(f"{l}\n")
                    f.write("</pre>")
                if matched_log_lines:
                    f.write("<h3>Log Output (Last 10 Lines)</h3><pre>")
                    for l in matched_log_lines:
                        for kw in log_kw_list:
                            if kw in l.lower():
                                l = l.replace(kw, f"<span class='keyword'>{kw}</span>")
                        f.write(f"{l}\n")
                    f.write("</pre>")
                f.write("</section>")

            # 이벤트 수집 (네임스페이스별 한번만)
            if namespace not in seen_namespaces:
                try:
                    event_json = json.loads(subprocess.getoutput(f"kubectl get events -n {namespace} -o json"))
                    all_events = event_json.get("items", [])
                    filtered = []
                    for e in all_events:
                        msg = e.get("message", "")
                        time_str = e.get("lastTimestamp") or e.get("eventTime") or e.get("firstTimestamp")
                        if not time_str:
                            continue
                        if any(kw in msg.lower() for kw in event_kw_list):
                            filtered.append({
                                "message": msg,
                                "type": e.get("type", ""),
                                "reason": e.get("reason", ""),
                                "time": time_str
                            })
                    # 시간순 내림차순 정렬
                    sorted_events = sorted(filtered, key=lambda x: x["time"], reverse=True)
                    if not sorted_events:
                        sorted_events = [{"message": "(No events matched)", "time": "", "type": "", "reason": ""}]
                    namespace_events[namespace] = sorted_events
                except Exception as e:
                    namespace_events[namespace] = [{"message": f"(Error parsing events: {str(e)})", "time": "", "type": "", "reason": ""}]
                seen_namespaces.add(namespace)

        # 이벤트 테이블 출력
        for ns, events in namespace_events.items():
            f.write(f"<section><h2>Namespace Events: {ns}</h2>")
            f.write(f"""<table id="events_{ns.replace('.', '-')}">
            <thead><tr>
            <th onclick="sortTable('events_{ns.replace('.', '-')}', 0)">Time</th>
            <th onclick="sortTable('events_{ns.replace('.', '-')}', 1)">Type</th>
            <th onclick="sortTable('events_{ns.replace('.', '-')}', 2)">Reason</th>
            <th onclick="sortTable('events_{ns.replace('.', '-')}', 3)">Message</th>
            </tr></thead><tbody>""")
            for e in events:
                highlight = "style='background-color:#ffdddd'" if any(kw in e.get("message", "").lower() for kw in event_kw_list) else ""
                f.write(f"<tr {highlight}><td>{e.get('time')}</td><td>{e.get('type')}</td><td>{e.get('reason')}</td><td>{e.get('message')}</td></tr>")
            f.write("</tbody></table></section>")

        f.write("</body></html>")

    # 결과를 output_report 경로로 복사
    os.rename(tmp_report_path, output_report.path)
