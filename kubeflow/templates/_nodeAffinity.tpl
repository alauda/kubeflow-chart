{{- define "kubeflow.nodeAffinity" }}
{{ if .Values.controlPlane.nodeAffinityKey }}
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: {{ .Values.controlPlane.nodeAffinityKey }}
          operator: In
          values: {{ .Values.controlPlane.nodeAffinityValues }}
{{ end }}
{{ end -}}
