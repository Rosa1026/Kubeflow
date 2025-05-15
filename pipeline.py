from kfp import dsl
from kfp import compiler
from collect_filtered_logs import collect_filtered_logs  # Import the component
from upload_to_github import upload_to_github  # Import the component

@dsl.pipeline(name="pod-log-pipeline-advance-version")
def cluster_health_report_pipeline(
    log_keywords: str = "CrashLoopBackOff,OOMKilled,evicted,failed to start,deadline exceeded,node not ready",
    event_keywords: str = "BackOff,FailedScheduling,NodeNotReady,Evicted,OutOfmemory",
    repo_url: str = "https://github.com/Rosa1026/Kubeflow.git",
    github_token: str = "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",
    branch: str = "report"
):

    report = collect_filtered_logs(
        log_keywords=log_keywords,
        event_keywords=event_keywords
    ).set_caching_options(False)

    upload_to_github(
        report_file=report.output,
        repo_url=repo_url,
        github_token=github_token,
        branch=branch
    ).set_caching_options(False)
