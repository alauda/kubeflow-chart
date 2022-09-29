{{- define "knserving.imagePullSecret" }}
{{- with .Values.global }}
{{- if .useRegistryCredentials }}
apiVersion: v1
kind: Secret
metadata:
  name: knserving-image-pull-secrets
  namespace: knative-serving
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: {{- printf "{\"auths\":{\"%s\":{\"username\":\"%s\",\"password\":\"%s\",\"email\":\"%s\",\"auth\":\"%s\"}}}" .registry .username .password .email (printf "%s:%s" .username .password | b64enc) | b64enc -}}
---
{{ end -}}
{{ end -}}
{{ end -}}