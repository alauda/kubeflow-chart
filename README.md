# Kubeflow Helm chart compatible with Cisco Calisti service Mesh

This repository provides a Helm chart definition for a Kubeflow base installation on top of the Cisco Calisti service mesh, for a generic Kubernetes cluster.


## Requirements

Prior to the Kubeflow deployment, you will need to install the following:
- the Helm package manager (https://helm.sh/)
- the Calisti service mesh (https://www.calisti.app/)

## Installation

After having deployed the Cisco Calisti service mesh, deploy the Kubeflow application by simply running
```
helm install kubeflow kubeflow/
```
Finally, install the post-installation resources by running
```
kubectl apply -f post_install/
```

