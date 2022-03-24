# Kubeflow Chart

使用 Helm Chart 在多种环境快速安装和配置 Kubeflow。

原始代码参考：https://github.com/kubeflow/manifests。

安装步骤：

- `git clone https://github.com/alauda/kubeflow-chart.git`
- 编辑 `kubeflow/values.yaml` 文件，针对不同的安装环境配置。
- 安装前置依赖 istio 和 cert-manager (如果已有则可跳过):
  - `helm install istio istio`
  - `helm install cert-manager certmanager`
- 安装 Kubeflow: `helm install kubeflow kubeflow`

访问 Kubeflow 界面：

- 通过 port-forward 方式：`kubectl port-forward svc/istio-ingressgateway -n istio-system --address=0.0.0.0 443:443`， 然后访问执行该命令的服务器地址：`https://ip/`。
- 通过 node port 方式：查看 istio ingressgateway 服务是否开启了 nodeport：`kubectl -n istio-system get svc istio-ingressgateway`，根据[这里](https://kubernetes.io/zh/docs/concepts/services-networking/service/#type-nodeport) 配置 nodeport 之后，即可访问。
- 使用 Ingress/LoadBalancer：配置 Ingress/LoadBalancer 到 istio-system/istio-ingressgateway 之后访问。


## 配置解释

建设中……
