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
  
### Use alternative image registry (for CN access)

When installing istio and cert-manager:

```bash
wget -O values-istio-cn.yaml https://raw.githubusercontent.com/alauda/kubeflow-chart/charts/istio/values-cn.yaml
helm install istio alauda/istio -f values-istio-cn.yaml
wget -O values-certm-cn.yaml https://raw.githubusercontent.com/alauda/kubeflow-chart/charts/certmanager/values-cn.yaml
helm install cert-manager alauda/certmanager -f values-certm-cn.yaml
```

Change the Kubeflow installation command as follows:

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
- Through ingress/LoadBalancer: configure your ingress/LoadBalancer to service `istio-system/istio-ingressgateway`.

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
