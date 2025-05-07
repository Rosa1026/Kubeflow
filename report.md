# 장애 복기 리포트
**Pod**: toolbox

## describe
```text
Name:         toolbox
Namespace:    istio-system
Priority:     0
Node:         k8s-kubeflow-worker02/192.168.2.233
Start Time:   Mon, 28 Apr 2025 06:15:24 +0000
Labels:       <none>
Annotations:  <none>
Status:       Running
IP:           10.244.1.238
IPs:
  IP:  10.244.1.238
Containers:
  toolbox:
    Container ID:   cri-o://a7f6c85a131aa257b81246351216d8076b43aa85294c6b5766d8f39e5cd3b44a
    Image:          mechpen/toolbox
    Image ID:       docker.io/mechpen/toolbox@sha256:cc82e7cc8ced5874fb1740c6006e2c28e6522dcc592b86f41076a122ed7cbfea
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Mon, 28 Apr 2025 06:16:00 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7pqcf (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-7pqcf:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:                      <none>
```
## logs
```text

```
## events
```text
LAST SEEN   TYPE      REASON                    OBJECT                                              MESSAGE
3m23s       Warning   FailedGetResourceMetric   horizontalpodautoscaler/cluster-local-gateway       failed to get cpu utilization: unable to get metrics for resource cpu: unable to fetch metrics from resource metrics API: the server could not find the requested resource (get pods.metrics.k8s.io)
4m23s       Warning   FailedGetResourceMetric   horizontalpodautoscaler/istio-ingressgateway        failed to get cpu utilization: unable to get metrics for resource cpu: unable to fetch metrics from resource metrics API: the server could not find the requested resource (get pods.metrics.k8s.io)
4m23s       Warning   FailedGetResourceMetric   horizontalpodautoscaler/istiod                      failed to get cpu utilization: unable to get metrics for resource cpu: unable to fetch metrics from resource metrics API: the server could not find the requested resource (get pods.metrics.k8s.io)
57m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110075-b9tj8   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110075-b9tj8 to k8s-kubeflow-worker02
57m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110075-b9tj8   Container image "docker.io/curlimages/curl" already present on machine
57m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110075-b9tj8   Created container: kubeflow-m2m-oidc-configurator
57m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110075-b9tj8   Started container kubeflow-m2m-oidc-configurator
57m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110075         Created pod: kubeflow-m2m-oidc-configurator-29110075-b9tj8
57m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110075         Job completed
52m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110080-7wz8n   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110080-7wz8n to k8s-kubeflow-worker01
52m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110080-7wz8n   Container image "docker.io/curlimages/curl" already present on machine
52m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110080-7wz8n   Created container: kubeflow-m2m-oidc-configurator
52m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110080-7wz8n   Started container kubeflow-m2m-oidc-configurator
52m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110080         Created pod: kubeflow-m2m-oidc-configurator-29110080-7wz8n
52m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110080         Job completed
47m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110085-8hvjx   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110085-8hvjx to k8s-kubeflow-worker01
47m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110085-8hvjx   Container image "docker.io/curlimages/curl" already present on machine
47m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110085-8hvjx   Created container: kubeflow-m2m-oidc-configurator
47m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110085-8hvjx   Started container kubeflow-m2m-oidc-configurator
47m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110085         Created pod: kubeflow-m2m-oidc-configurator-29110085-8hvjx
47m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110085         Job completed
42m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110090-787ff   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110090-787ff to k8s-kubeflow-worker02
42m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110090-787ff   Container image "docker.io/curlimages/curl" already present on machine
42m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110090-787ff   Created container: kubeflow-m2m-oidc-configurator
42m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110090-787ff   Started container kubeflow-m2m-oidc-configurator
42m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110090         Created pod: kubeflow-m2m-oidc-configurator-29110090-787ff
42m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110090         Job completed
37m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110095-mmsb9   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110095-mmsb9 to k8s-kubeflow-worker02
37m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110095-mmsb9   Container image "docker.io/curlimages/curl" already present on machine
37m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110095-mmsb9   Created container: kubeflow-m2m-oidc-configurator
37m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110095-mmsb9   Started container kubeflow-m2m-oidc-configurator
37m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110095         Created pod: kubeflow-m2m-oidc-configurator-29110095-mmsb9
37m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110095         Job completed
32m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110100-hp982   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110100-hp982 to k8s-kubeflow-worker01
32m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110100-hp982   Container image "docker.io/curlimages/curl" already present on machine
32m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110100-hp982   Created container: kubeflow-m2m-oidc-configurator
32m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110100-hp982   Started container kubeflow-m2m-oidc-configurator
32m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110100         Created pod: kubeflow-m2m-oidc-configurator-29110100-hp982
32m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110100         Job completed
27m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110105-s8m7w   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110105-s8m7w to k8s-kubeflow-worker02
27m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110105-s8m7w   Container image "docker.io/curlimages/curl" already present on machine
27m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110105-s8m7w   Created container: kubeflow-m2m-oidc-configurator
27m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110105-s8m7w   Started container kubeflow-m2m-oidc-configurator
27m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110105         Created pod: kubeflow-m2m-oidc-configurator-29110105-s8m7w
27m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110105         Job completed
22m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110110-lv2sz   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110110-lv2sz to k8s-kubeflow-worker02
22m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110110-lv2sz   Container image "docker.io/curlimages/curl" already present on machine
22m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110110-lv2sz   Created container: kubeflow-m2m-oidc-configurator
22m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110110-lv2sz   Started container kubeflow-m2m-oidc-configurator
22m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110110         Created pod: kubeflow-m2m-oidc-configurator-29110110-lv2sz
22m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110110         Job completed
17m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110115-7hdqq   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110115-7hdqq to k8s-kubeflow-worker02
17m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110115-7hdqq   Container image "docker.io/curlimages/curl" already present on machine
17m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110115-7hdqq   Created container: kubeflow-m2m-oidc-configurator
17m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110115-7hdqq   Started container kubeflow-m2m-oidc-configurator
17m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110115         Created pod: kubeflow-m2m-oidc-configurator-29110115-7hdqq
17m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110115         Job completed
12m         Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110120-wsnml   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110120-wsnml to k8s-kubeflow-worker02
12m         Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110120-wsnml   Container image "docker.io/curlimages/curl" already present on machine
12m         Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110120-wsnml   Created container: kubeflow-m2m-oidc-configurator
12m         Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110120-wsnml   Started container kubeflow-m2m-oidc-configurator
12m         Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110120         Created pod: kubeflow-m2m-oidc-configurator-29110120-wsnml
12m         Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110120         Job completed
7m37s       Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110125-9xwrp   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110125-9xwrp to k8s-kubeflow-worker02
7m37s       Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110125-9xwrp   Container image "docker.io/curlimages/curl" already present on machine
7m37s       Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110125-9xwrp   Created container: kubeflow-m2m-oidc-configurator
7m37s       Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110125-9xwrp   Started container kubeflow-m2m-oidc-configurator
7m37s       Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110125         Created pod: kubeflow-m2m-oidc-configurator-29110125-9xwrp
7m29s       Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110125         Job completed
2m37s       Normal    Scheduled                 pod/kubeflow-m2m-oidc-configurator-29110130-kq86r   Successfully assigned istio-system/kubeflow-m2m-oidc-configurator-29110130-kq86r to k8s-kubeflow-worker02
2m37s       Normal    Pulled                    pod/kubeflow-m2m-oidc-configurator-29110130-kq86r   Container image "docker.io/curlimages/curl" already present on machine
2m37s       Normal    Created                   pod/kubeflow-m2m-oidc-configurator-29110130-kq86r   Created container: kubeflow-m2m-oidc-configurator
2m37s       Normal    Started                   pod/kubeflow-m2m-oidc-configurator-29110130-kq86r   Started container kubeflow-m2m-oidc-configurator
2m37s       Normal    SuccessfulCreate          job/kubeflow-m2m-oidc-configurator-29110130         Created pod: kubeflow-m2m-oidc-configurator-29110130-kq86r
2m29s       Normal    Completed                 job/kubeflow-m2m-oidc-configurator-29110130         Job completed
2m37s       Normal    SuccessfulCreate          cronjob/kubeflow-m2m-oidc-configurator              (combined from similar events): Created job kubeflow-m2m-oidc-configurator-29110130
```
