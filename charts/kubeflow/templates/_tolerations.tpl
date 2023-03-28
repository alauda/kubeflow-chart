{{- define "kubeflow.tolerations" }}
{{ if .Values.controlPlane.tolerationsKeys }}
{{ range .Values.controlPlane.tolerationsKeys }}
tolerations:
- key: "{{ . }}"
  operator: "Exists"
  effect: "NoSchedule"
{{ end }}
{{ end }}
{{ end -}}