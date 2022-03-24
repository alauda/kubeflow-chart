# Kubeflow Chart

Helm chart to install Kubeflow on your Kubernetes Cluster.

Steps to install:


- `git clone https://github.com/alauda/kubeflow-chart.git`
- Setup `kubeflow/values.yaml` for your environment.
- Install dependencies (optional):
  - `helm install istio istio`
  - `helm install cert-manager certmanager`
- Install Kubeflow: `helm install kubeflow kubeflow`

That's it!


