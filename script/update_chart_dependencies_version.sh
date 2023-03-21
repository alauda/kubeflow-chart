#!/usr/bin/env bash
set -e

root_dir=$(dirname $(dirname $(realpath $0)))
chart_dir=${root_dir}/charts

length=$(yq '.dependencies | length' ${chart_dir}/kubeflow/Chart.yaml)
number=0
while [[ ${number} -lt ${length} ]] ; do
    name=$(echo ${number} | xargs -I {} yq e '.dependencies[{}].name' ${chart_dir}/kubeflow/Chart.yaml)
    version=$(echo ${name} | xargs -I {} yq e '.version' ${chart_dir}/kubeflow/charts/{}/Chart.yaml)
    eval "yq e '.dependencies["${number}"].version = \""${version}"\"' -i ${chart_dir}/kubeflow/Chart.yaml"
    ((number = number + 1))
done
