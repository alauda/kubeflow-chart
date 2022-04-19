# Kubeflow Chart

使用 Helm Chart 在多种环境更加快速安装和配置 [Kubeflow](https://www.kubeflow.org/)。

作为 [kubeflow manifests](https://github.com/kubeflow/manifests) 的另一种开源部署方式，您可以轻松快速的在任意环境（公有云，本地集群，minikube）之上部署并运行 Kubeflow。

安装步骤(minikube)：

- `git clone https://github.com/alauda/kubeflow-chart.git`
- 编辑 `kubeflow/values.yaml` 文件，针对不同的安装环境配置。
- 安装前置依赖 istio 和 cert-manager (如果已有则可跳过):
  - `helm install istio istio`
  - `helm install cert-manager certmanager`
- 安装 Kubeflow: `helm install kubeflow-helm kubeflow`
- 如果需要使用国内镜像源，可以用下面的命令：
  `helm install kubeflow-helm kubeflow -f values-cn.yaml`

访问 Kubeflow 界面：

- 通过 port-forward 方式：`kubectl port-forward svc/istio-ingressgateway -n istio-system --address=0.0.0.0 443:443`， 然后访问执行该命令的服务器地址：`https://ip/`。
- 通过 node port 方式：查看 istio ingressgateway 服务是否开启了 nodeport：`kubectl -n istio-system get svc istio-ingressgateway`，根据[这里](https://kubernetes.io/zh/docs/concepts/services-networking/service/#type-nodeport) 配置 nodeport 之后，即可访问。
- 使用 Ingress/LoadBalancer：配置 Ingress/LoadBalancer 到 istio-system/istio-ingressgateway 之后访问。


## 配置

### 使用 HTTPS

Kubeflow 强依赖 HTTPS，只有使用 `localhost` 访问可以不使用 HTTPS。

需要配置 HTTPS 时，请配置 `values.yaml` 中的 `tlsCrt` 和 `tlsKey` 为 HTTPS 证书。

### 配置 Dex 登录认证

如果不使用本 chart 内置的 dex 部署，即需要连接到已有的 dex 部署，需要：

1. 修改 `dex: enabled: false`
2. 修改 `values.yaml` 下面的选项已联通您已有的 dex：
```
# 配置和认证服务 Dex 的联动
oidcAuthURL: /dex/auth
oidcProvider: http://dex.auth.svc.cluster.local:5556/dex
oidcRedirectURL: /login/oidc
skipAuthURI: "/dex"
useridClaim: email
useridHeader: kubeflow-userid
useridPrefix: "\"\""
oidcScopes: "profile email groups"
```


## TODO

- 适配 `cert-manager`, `istio`, `dex`, `minio` 的官方 Charts
- 统一 `values.yaml` 中的 镜像/tag 的配置
