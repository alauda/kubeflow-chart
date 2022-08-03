images_to_push = [
    [
        "gcr.io/ml-pipeline/minio",
        "minio",
        "RELEASE.2019-08-14T20-37-41Z-license-compliance"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/admission-webhook",
        "admission-webhook",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/jupyter-web-app",
        "jupyter-web-app",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/notebook-controller",
        "notebook-controller",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-scipy",
        "jupyter-scipy",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-pytorch-full",
        "jupyter-pytorch-full",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-pytorch-cuda-full",
        "jupyter-pytorch-cuda-full",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-tensorflow-full",
        "jupyter-tensorflow-full",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/jupyter-tensorflow-cuda-full",
        "jupyter-tensorflow-cuda-full",
        "v1.5.0"
    ],
    [
        "gcr.io/arrikto/kubeflow/oidc-authservice",
        "oidc-authservice",
        "28c59ef"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/central-dashboard",
        "central-dashboard",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/access-management",
        "access-management",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/profile-controller",
        "profile-controller",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/volumes-web-app",
        "volumes-web-app",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/codeserver-python",
        "codeserver-python",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/notebook-servers/rstudio-tidyverse",
        "rstudio-tidyverse",
        "v1.5.0"
    ],
    [
        "gcr.io/ml-pipeline/api-server",
        "api-server",
        "1.8.2"
    ],
    [
        "gcr.io/ml-pipeline/kfp-launcher",
        "kfp-launcher",
        "1.7.1"
    ],
    [
        "gcr.io/ml-pipeline/visualization-server",
        "visualization-server",
        "1.8.2"
    ],
    [
        "gcr.io/ml-pipeline/frontend",
        "frontend",
        "1.8.2"
    ],
    [
        "gcr.io/ml-pipeline/viewer-crd-controller",
        "viewer-crd-controller",
        "1.8.2"
    ],
    [
        "gcr.io/ml-pipeline/scheduledworkflow",
        "scheduledworkflow",
        "1.8.2"
    ],
    [
        "gcr.io/ml-pipeline/persistenceagent",
        "persistenceagent",
        "1.8.2"
    ],
    [
        "gcr.io/ml-pipeline/metadata-writer",
        "metadata-writer",
        "1.8.2"
    ],
    [
        "gcr.io/ml-pipeline/metadata-envoy",
        "metadata-envoy",
        "1.8.2"
    ],
    [
        "gcr.io/ml-pipeline/cache-server",
        "cache-server",
        "1.8.2"
    ],
    [
        "gcr.io/tfx-oss-public/ml_metadata_store_server",
        "ml_metadata_store_server",
        "1.5.0"
    ],
    [
        "gcr.io/google-containers/busybox",
        "busybox",
        "latest"
    ],
    [
        "gcr.io/ml-pipeline/argoexec",
        "argoexec",
        "v3.2.3-license-compliance"
    ],
    [
        "gcr.io/ml-pipeline/workflow-controller",
        "workflow-controller",
        "v3.2.3-license-compliance"
    ],
    [
        "metacontroller/metacontroller",
        "metacontroller",
        "v2.0.4"
    ],
    [
        "gcr.io/ml-pipeline/mysql",
        "mysql",
        "5.7"
    ],
    [
        "python",
        "python",
        "3.7"
    ],
    [
        "kserve/agent",
        "agent",
        "v0.7.0"
    ],
    [
        "kserve/alibi-explainer",
        "alibi-explainer",
        "v0.7.0"
    ],
    [
        "kserve/aix-explainer",
        "aix-explainer",
        "v0.7.0"
    ],
    [
        "kserve/art-explainer",
        "art-explainer",
        "v0.7.0"
    ],
    [
        "tensorflow/serving",
        "tensorflow-serving",
        "1.14.0"
    ],
    [
        "tensorflow/serving",
        "tensorflow-serving",
        "1.14.0-gpu"
    ],
    [
        "mcr.microsoft.com/onnxruntime/server",
        "onnx-server",
        "v1.0.0"
    ],
    [
        "kserve/sklearnserver",
        "sklearnserver",
        "v0.7.0"
    ],
    [
        "docker.io/seldonio/mlserver",
        "mlserver",
        "0.2.1"
    ],
    [
        "kserve/xgbserver",
        "xgbserver",
        "v0.7.0"
    ],
    [
        "kserve/pytorchserver",
        "pytorchserver",
        "v0.7.0"
    ],
    [
        "kserve/pytorchserver",
        "pytorchserver",
        "v0.7.0-gpu"
    ],
    [
        "pytorch/torchserve-kfs",
        "torchserve-kfs",
        "0.4.1"
    ],
    [
        "pytorch/torchserve-kfs",
        "torchserve-kfs",
        "0.4.1-gpu"
    ],
    [
        "nvcr.io/nvidia/tritonserver",
        "tritonserver",
        "21.09-py3"
    ],
    [
        "kserve/pmmlserver",
        "pmmlserver",
        "v0.7.0"
    ],
    [
        "kserve/lgbserver",
        "lgbserver",
        "v0.7.0"
    ],
    [
        "kserve/paddleserver",
        "paddleserver",
        "v0.7.0"
    ],
    [
        "kserve/storage-initializer",
        "storage-initializer",
        "v0.7.0"
    ],
    [
        "kserve/models-web-app",
        "models-web-app",
        "v0.7.0"
    ],
    [
        "kserve/kserve-controller",
        "kserve-controller",
        "v0.7.0"
    ],
    [
        "gcr.io/kubebuilder/kube-rbac-proxy",
        "kube-rbac-proxy",
        "v0.4.0"
    ],
    [
        "gcr.io/knative-releases/knative.dev/serving/cmd/queue",
        "queue",
        "v0.22.1"
    ],
    [
        "gcr.io/knative-releases/knative.dev/serving/cmd/activator",
        "activator",
        "v0.22.1"
    ],
    [
        "gcr.io/knative-releases/knative.dev/serving/cmd/autoscaler",
        "autoscaler",
        "v0.22.1"
    ],
    [
        "gcr.io/knative-releases/knative.dev/serving/cmd/controller",
        "knative-serving-controller",
        "v0.22.1"
    ],
    [
        "gcr.io/knative-releases/knative.dev/net-istio/cmd/webhook",
        "knative-net-istio-webhook",
        "v0.22.1"
    ],
    [
        "gcr.io/knative-releases/knative.dev/net-istio/cmd/controller",
        "knative-net-istio-controller",
        "v0.22.1"
    ],
    [
        "gcr.io/knative-releases/knative.dev/serving/cmd/webhook",
        "knative-serving-webhook",
        "v0.22.1"
    ],
    [
        "docker.io/istio/proxyv2",
        "proxyv2",
        "1.11.4"
    ],
    [
        "docker.io/istio/pilot",
        "pilot",
        "1.11.4"
    ],
    [
        "public.ecr.aws/j1r0q0g6/training/training-operator",
        "training-operator",
        "174e8813666951ded505daf334a37f60fd50c18d"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/tensorboard-controller",
        "tensorboard-controller",
        "v1.5.0"
    ],
    [
        "public.ecr.aws/j1r0q0g6/notebooks/tensorboards-web-app",
        "tensorboards-web-app",
        "v1.5.0"
    ],
    [
        "quay.io/jetstack/cert-manager-controller",
        "cert-manager-controller",
        "v1.5.0"
    ],
    [
        "quay.io/jetstack/cert-manager-cainjector",
        "cert-manager-cainjector",
        "v1.5.0"
    ],
    [
        "quay.io/jetstack/cert-manager-webhook",
        "cert-manager-webhook",
        "v1.5.0"
    ],
    [
        "quay.io/dexidp/dex",
        "dex",
        "v2.24.0"
    ],
]

images_to_push = [
    [
        "kserve/kserve-controller",
        "kserve-controller",
        "v0.7.0"
    ],
    [
        "kserve/models-web-app",
        "models-web-app",
        "v0.7.0"
    ],
]

def check_target_image_dup():
    target_image_names = set()
    dup_names = []
    for i in images_to_push:
        n = i[1] + ":" + i[2]
        if n in target_image_names:
            dup_names.append(n)
        else:
            target_image_names.add(n)
    if len(dup_names):
        raise Exception("target image repo duplication detected: %s" % dup_names)

check_target_image_dup()

target_repo = "registry.cn-hangzhou.aliyuncs.com/kubeflow-chart"
values_in = "charts/kubeflow/values.yaml"
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

for m in images_to_push:
    img, tgt, tag = m
    if not tag:
        errors.append("have no tag: %s, skipping..." % img)
        continue
    orig_img = ":".join([img, tag])
    target_image = target_repo + "/" + tgt + ":" + tag
    if push:
        os.system("docker pull %s" % orig_img)
        os.system("docker tag %s %s" % (orig_img, target_image))
        print("pushing src(%s) ->  %s" % (orig_img, target_image))
        os.system("docker push %s" % target_image)
        # os.system("docker rmi %s" % target_image)
        os.system("docker rmi %s" % orig_img)
    
    # FIXME: minio image configuration is under a sub-chart
    if tgt == "minio":
        values_out_obj["minio"] = {"kfpMinioImage": target_image}
    if tgt == "dex":
        values_out_obj["dex"] = {"dexImage": target_image}
    else:
        img_key, has_tag = find_image_value_key(img, tag)
        if img_key != None:
            values_out_obj[img_key] = target_image
        else:
            errors.append("%s not found in values.yaml" % orig_img)

out_yaml = yaml.dump(values_out_obj, Dumper=Dumper)
print(out_yaml)
print("--------")
print("errors: ", errors)
