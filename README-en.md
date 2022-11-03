# Kubeflow Chart

Install [Kubeflow](https://www.kubeflow.org/) on various environments using [Helm](https://helm.sh/).

As an alternative of [kubeflow manifests](https://github.com/kubeflow/manifests), you can deploy
Kubeflow at any environments using Helm.

## Quick Installation(Using local Minikube)：

1. `helm repo add alauda https://alauda.github.io/kubeflow-chart`
1. `helm install kubeflow alauda/kubeflow`
  
### Use alternative image registry (for CN access)

Use `values-cn.yaml` to override image configurations:

```bash
wget -O values-cn.yaml https://raw.githubusercontent.com/alauda/kubeflow-chart/main/values-cn.yaml
helm install kubeflow alauda/kubeflow -f values-cn.yaml
```

### Access Kubeflow Web UI:

Start a port-forward:

```bash
kubectl port-forward svc/istio-ingressgateway -n istio-system --address=0.0.0.0 8080:80
```

Visit `http://localhost:8080/`.

### Configure using a private registry:

If you have pushed images to your private image registry, setup below fields:
```yaml
global:
  imageCredentials: ""
  useRegistryCredentials: false
  registry: quay.io
  username: someone
  password: sillyness
  email: someone@host.com
minio:
  useKubeflowImagePullSecrets: true
```

## Uninstall Kubeflow

Run `helm delete kubeflow` to uninstall Kubeflow.

## Deploy Kubeflow in production

To deploy Kubeflow in a production Kubernetes cluster, you need to configure below settings:

### Setup HTTPS

You ***Must*** use HTTPS to access Kubeflow web UI. Only when you deploy it under `localhost`, you do not need to setup HTTPS settings.

To setup HTTPS, configure `tlsCrt` and `tlsKey` to be the HTTPS `.crt` and `.key` file content (base64 encoded).

### Setup Access To the UI

Kubeflow uses [Istio](https://istio.io/) as the service mesh control, you should configure you cluster load balancer or ingress to redirect to istio-ingressgateway:

- Through port-forward (***not recommended***):
  - HTTP: `kubectl port-forward svc/istio-ingressgateway -n istio-system --address=0.0.0.0 8080:80`, then browse `http://ip:8080/`.
  - HTTPS: `kubectl port-forward svc/istio-ingressgateway -n istio-system --address=0.0.0.0 443:443`, then browse `https://ip/`
- The default username and password is: `user@example.com`, `12341234`
- Through [NodePort](https://kubernetes.io/zh/docs/concepts/services-networking/service/#type-nodeport): first checkout if your `ingressgateway` service is running with NodePort: `kubectl -n istio-system get svc istio-ingressgateway`. Then access the NodePort to open Kubeflow web UI.
- Through Ingress: If Ingress is available in your cluster, then set `enableIngress: true` and
  `kubeflowHost` to your domain name in `values.yaml`, e.g. `kubeflowHost: "kubeflow.test.info"`.

### Setup Dex Authentication (Optional)

If need to connect Kubeflow to you current Dex deployment, you may need to setup below sections under `values.yaml`:

1. change `dex: enabled: false`
2. Setup below sections to connect to your Dex:
```
oidcAuthURL: /dex/auth
oidcProvider: http://dex.auth.svc.cluster.local:5556/dex
oidcRedirectURL: /login/oidc
skipAuthURI: "/dex"
useridClaim: email
useridHeader: kubeflow-userid
useridPrefix: "\"\""
oidcScopes: "profile email groups"

clientID: <your-dex-clientID>
clientSecret: <your-dex-client-secret>
```

## TODO

- Let `cert-manager`, `istio`, `dex`, `minio` to be the sub-chart of Kubeflow
- Unify Docker image/tag settings in `values.yaml`
- Supports subpath of Kubeflow URL access, like: `https://domain.name/kubeflow/`
