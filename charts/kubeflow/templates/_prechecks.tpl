{{ define "prechecks" }}

{{ if .Values.checkDeps }}

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

{{ $istioIngDeploy := lookup "apps/v1" "Deployment" "istio-system" "istio-ingressgateway" }}
{{ if not $istioIngDeploy }}
{{ fail "must install istio-ingressgateway deployment (install ASM on ACP)" }}
{{ end }}
{{ $istioEgDeploy := lookup "apps/v1" "Deployment" "istio-system" "istio-egressgateway" }}
{{ if not $istioEgDeploy }}
{{ fail "must install istio-egressgateway deployment (install ASM on ACP)" }}
{{ end }}
{{ $istiodDeploy := lookup "apps/v1" "Deployment" "istio-system" "istiod" }}
{{ $istiodDeploy110 := lookup "apps/v1" "Deployment" "istio-system" "istiod-1-10" }}
{{ $istiodDeploy112 := lookup "apps/v1" "Deployment" "istio-system" "istiod-1-12" }}
{{ if not (or $istiodDeploy $istiodDeploy110 $istiodDeploy112) }}
{{ fail "must install istiod deployment (install ASM on ACP)" }}
{{ end }}

{{/* Check if cert-manager is installed */}}
{{ $certMngrNamespace := lookup "v1" "Namespace" "" "cert-manager" }}
{{ if not $certMngrNamespace }}
{{ fail "must install cert-manager namespace" }}
{{ end }}

{{ $certMngrDeploy := lookup "apps/v1" "Deployment" "cert-manager" "cert-manager" }}
{{ if not $certMngrDeploy }}
{{ fail "must install cert-manager deployment" }}
{{ end }}
{{ $certMngrCJDeploy := lookup "apps/v1" "Deployment" "cert-manager" "cert-manager-cainjector" }}
{{ if not $certMngrCJDeploy }}
{{ fail "must install cert-manager-cainjector deployment" }}
{{ end }}
{{ $certMngrWHDeploy := lookup "apps/v1" "Deployment" "cert-manager" "cert-manager-webhook" }}
{{ if not $certMngrWHDeploy }}
{{ fail "must install cert-manager-webhook deployment" }}
{{ end }}

{{ end }}

{{ end }}
