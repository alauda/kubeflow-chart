images_to_push = [
"gcr.io/ml-pipeline/minio:RELEASE.2019-08-14T20-37-41Z-license-compliance",
"public.ecr.aws/j1r0q0g6/notebooks/admission-webhook:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/jupyter-web-app:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/notebook-controller:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-scipy:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-pytorch-full:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-pytorch-cuda-full:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-tensorflow-full:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-tensorflow-cuda-full:v1.4",
"gcr.io/arrikto/kubeflow/oidc-authservice:28c59ef",
"public.ecr.aws/j1r0q0g6/notebooks/central-dashboard:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/access-management:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/profile-controller:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/volumes-web-app:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/codeserver-python:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/rstudio-tidyverse:v1.4",
"gcr.io/ml-pipeline/api-server:1.7.0",
"gcr.io/ml-pipeline/kfp-launcher:1.7.1",
"gcr.io/ml-pipeline/visualization-server:1.7.0",
"gcr.io/ml-pipeline/frontend:1.7.0",
"gcr.io/ml-pipeline/viewer-crd-controller:1.7.0",
"gcr.io/ml-pipeline/scheduledworkflow:1.7.0",
"gcr.io/ml-pipeline/persistenceagent:1.7.0",
"gcr.io/ml-pipeline/metadata-writer:1.7.0",
"gcr.io/ml-pipeline/metadata-envoy:1.7.0",
"gcr.io/ml-pipeline/cache-server:1.7.0",
"gcr.io/ml-pipeline/cache-deployer:1.7.0",
"gcr.io/tfx-oss-public/ml_metadata_store_server:1.0.0",
"gcr.io/google-containers/busybox",
"gcr.io/ml-pipeline/argoexec:v3.1.6-patch-license-compliance",
"gcr.io/ml-pipeline/workflow-controller:v3.1.6-patch-license-compliance",
"metacontroller/metacontroller:v0.3.0",
"gcr.io/ml-pipeline/mysql:5.7",
"python:3.7",
"kfserving/agent:v0.6.1",
"kfserving/alibi-explainer:v0.6.1",
"kfserving/aix-explainer:v0.6.1",
"kfserving/art-explainer:v0.6.1",
"tensorflow/serving:1.14.0",
"tensorflow/serving:1.14.0-gpu",
"mcr.microsoft.com/onnxruntime/server:v1.0.0",
"kfserving/sklearnserver:v0.6.1",
"docker.io/seldonio/mlserver:0.2.1",
"kfserving/xgbserver:v0.6.1",
"kfserving/pytorchserver:v0.6.1",
"kfserving/pytorchserver:v0.6.1-gpu",
"pytorch/torchserve-kfs:0.4.0",
"pytorch/torchserve-kfs:0.4.0-gpu",
"nvcr.io/nvidia/tritonserver:20.08-py3",
"kfserving/pmmlserver:v0.6.1",
"kfserving/lgbserver:v0.6.1",
"kfserving/paddleserver:v0.6.1",
"kfserving/storage-initializer:v0.6.1",
"kfserving/models-web-app:v0.6.1",
"kfserving/kfserving-controller:v0.6.1",
"gcr.io/kubebuilder/kube-rbac-proxy:v0.4.0",
"gcr.io/knative-releases/knative.dev/serving/cmd/queue:v0.22.1",
"gcr.io/knative-releases/knative.dev/serving/cmd/activator:v0.22.1",
"gcr.io/knative-releases/knative.dev/serving/cmd/autoscaler:v0.22.1",
"gcr.io/knative-releases/knative.dev/serving/cmd/controller:v0.22.1",
"gcr.io/knative-releases/knative.dev/net-istio/cmd/webhook:v0.22.1",
"gcr.io/knative-releases/knative.dev/net-istio/cmd/controller:v0.22.1",
"gcr.io/knative-releases/knative.dev/serving/cmd/webhook:v0.22.1",
"docker.io/istio/proxyv2:1.9.6",
"public.ecr.aws/j1r0q0g6/training/training-operator:760ac1171dd30039a7363ffa03c77454bd714da5",
"mpioperator/mpi-operator:0.3.0",
"mpioperator/kubectl-delivery:latest",
"public.ecr.aws/j1r0q0g6/notebooks/tensorboard-controller:v1.4",
"public.ecr.aws/j1r0q0g6/notebooks/tensorboards-web-app:v1.4"
]

target_repo = "registry.cn-hangzhou.aliyuncs.com/kubeflow-chart"
values_in = "kubeflow/values.yaml"
values_out = "./values-cn.yaml"
push = True

import os
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

values_out_obj = {}
with open(values_in, "r") as fn:
    values_in_obj = yaml.load(fn, Loader=Loader)

def find_image_value_key(img, tag):
    img_tag = ":".join([img, tag])
    found_key = None
    has_tag = None
    for k in values_in_obj:
        v = values_in_obj[k]
        if type(v) == str:
            if v == img or v == img_tag:
                found_key = k
                if v == img:
                    has_tag = False
                if v == img_tag:
                    has_tag = True
                break
    return found_key, has_tag

errors = []

for orig_img in images_to_push:
    img_tag = orig_img.split(":")
    if len(img_tag) == 1:
        img = img_tag[0]
        tag = "latest"
    elif len(img_tag) == 2:
        img, tag = img_tag
    else:
        errors.append("error parsing image: %s" % orig_img)
    img_final_name = img.split("/")[-1]
    target_image = target_repo + "/" + img_final_name + ":" + tag
    if push:
        os.system("docker pull %s" % orig_img)
        os.system("docker tag %s %s" % (orig_img, target_image))
        print("pushing %s" % target_image)
        os.system("docker push %s" % target_image)
        os.system("docker rmi %s" % target_image)
        os.system("docker rmi %s" % orig_img)
    
    # FIXME: minio image configuration is under a sub-chart
    if img_final_name == "minio":
        values_out_obj["minio"] = {"kfpMinioImage": target_image}
    else:
        img_key, has_tag = find_image_value_key(img, tag)
        if img_key != None:
            if has_tag:
                values_out_obj[img_key] = target_image
            else:
                values_out_obj[img_key] = target_repo + "/" + img_final_name
        else:
            errors.append("%s not found in values.yaml" % orig_img)
    
out_yaml = yaml.dump(values_out_obj, Dumper=Dumper)
print(out_yaml)
print("--------")
print("errors: ", errors)
