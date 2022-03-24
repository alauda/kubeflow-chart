{{ define "prechecks" }}

{{ if not .Values.dryRun }}

{{/* Check if istio is installed. */}}
{{ $istioNamespace := lookup "v1" "Namespace" "" "istio-system" }}
{{ if not $istioNamespace }}
{{ fail "must install istio-system namespace (install ASM on ACP)" }}
{{ end }}
{{ $istioGatewaysCRD := lookup "apiextensions.k8s.io/v1" "CustomResourceDefinition" "" "gateways.networking.istio.io" }}
{{ if not $istioGatewaysCRD }}
{{ fail "must install gateways.networking.istio.io crd (install ASM on ACP)" }}
{{ end }}
{{ $istioVSCRD := lookup "apiextensions.k8s.io/v1" "CustomResourceDefinition" "" "virtualservices.networking.istio.io" }}
{{ if not $istioVSCRD }}
{{ fail "must install virtualservices.networking.istio.io crd (install ASM on ACP)" }}
{{ end }}
{{ $istioEnvoyCRD := lookup "apiextensions.k8s.io/v1" "CustomResourceDefinition" "" "envoyfilters.networking.istio.io" }}
{{ if not $istioEnvoyCRD }}
{{ fail "must install envoyfilters.networking.istio.io crd (install ASM on ACP)" }}
{{ end }}

{{ $istioIngDeploy := lookup "v1" "Deployment" "istio-system" "istio-ingressgateway" }}
{{ if not $istioIngDeploy }}
{{ fail "must install istio-ingressgateway deployment (install ASM on ACP)" }}
{{ end }}
{{ $istioEgDeploy := lookup "v1" "Deployment" "istio-system" "istio-egressgateway" }}
{{ if not $istioEgDeploy }}
{{ fail "must install istio-egressgateway deployment (install ASM on ACP)" }}
{{ end }}
{{ $istiodDeploy := lookup "v1" "Deployment" "istio-system" "istiod-1-10" }}
{{ if not $istiodDeploy }}
{{ fail "must install istiod-1-10 deployment (install ASM on ACP)" }}
{{ end }}

{{/* Check if cert-manager is installed */}}
{{ $certMngrNamespace := lookup "v1" "Namespace" "" "cert-manager" }}
{{ if not $certMngrNamespace }}
{{ fail "must install cert-manager namespace" }}
{{ end }}

{{ $certMngrDeploy := lookup "v1" "Deployment" "cert-manager" "cert-manager" }}
{{ if not $certMngrDeploy }}
{{ fail "must install cert-manager deployment" }}
{{ end }}
{{ $certMngrCJDeploy := lookup "v1" "Deployment" "cert-manager" "cert-manager-cainjector" }}
{{ if not $certMngrCJDeploy }}
{{ fail "must install cert-manager-cainjector deployment" }}
{{ end }}
{{ $certMngrWHDeploy := lookup "v1" "Deployment" "cert-manager" "cert-manager-webhook" }}
{{ if not $certMngrWHDeploy }}
{{ fail "must install cert-manager-webhook deployment" }}
{{ end }}

{{ end }}

{{ end }}
