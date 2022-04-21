# Kubeflow Chart

Install [Kubeflow](https://www.kubeflow.org/) on various environments using [Helm](https://helm.sh/).

As an alternative of [kubeflow manifests](https://github.com/kubeflow/manifests), you can deploy
Kubeflow at any environments using Helm.

## Quick Installation(Using local Minikube)：

1. `helm repo add alauda https://alauda.github.io/kubeflow-chart`
2. Install requirements (skip this step if already installed):
  - `helm install istio alauda/istio`
  - `helm install cert-manager alauda/certmanager`
3. `helm install my-kubeflow alauda/kubeflow`
  
### Use alternative image registry

Change the installation command as follows:

1. `wget https://raw.githubusercontent.com/alauda/kubeflow-chart/main/values-cn.yaml`
2. `helm install my-kubeflow alauda/kubeflow -f values-cn.yaml`

### Access Kubeflow Web UI:

Start a port-forward:

```bash
kubectl port-forward svc/istio-ingressgateway -n istio-system --address=0.0.0.0 8080:80
```

Visit `http://localhost:8080/`.

## Uninstall Kubeflow

Run `helm delete my-kubeflow` to uninstall Kubeflow.

## 在生产集群中部署 Kubeflow

在生产集群中部署 Kubeflow，通常需要根据当前集群环境信息，完成如下配置：

### 使用 HTTPS

Kubeflow 强依赖 HTTPS，只有使用 `localhost` 访问可以不使用 HTTPS，所以在使用 Minikube 快速部署时不需要配置 HTTPS 相关配置项。当需要配置 HTTPS 时，请配置 `values.yaml` 中的 `tlsCrt` 和 `tlsKey` 为 HTTPS 证书。

### 配置访问方式

- 通过 port-forward 方式（不推荐）：
  - 使用 HTTP: `kubectl port-forward svc/istio-ingressgateway -n istio-system --address=0.0.0.0 8080:80`， 然后访问执行该命令的服务器地址：`http://ip/`。
  - 开启 HTTPS: `kubectl port-forward svc/istio-ingressgateway -n istio-system --address=0.0.0.0 443:443`， 然后访问执行该命令的服务器地址：`https://ip/`。
- 使用默认账号密码：`user@example.com`, `12341234` 即可登录。
- 通过 node port 方式：查看 istio ingressgateway 服务是否开启了 nodeport：`kubectl -n istio-system get svc istio-ingressgateway`，根据[这里](https://kubernetes.io/zh/docs/concepts/services-networking/service/#type-nodeport) 配置 nodeport 之后，即可访问。
- 使用 Ingress/LoadBalancer：配置 Ingress/LoadBalancer 到 istio-system/istio-ingressgateway 之后访问。

### 配置 Dex 登录认证 (可选)

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
