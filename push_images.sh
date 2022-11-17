#!/bin/bash

DRYRUN=yes

lines=$(cat images-1.6.txt)
COUNTER=0
ORIG_IMG=""
NEW_IMG=""

for l in $lines
do
    if [ "${l}" == "" ]; then
    continue
    fi

    # echo $COUNTER, $l
    ORIG_IMG=$NEW_IMG
    NEW_IMG=$l
    if [[ "${NEW_IMG}" == registry.cn-hangzhou.aliyuncs.com/kubeflow-chart* ]]; then
        let COUNTER++
        echo "$COUNTER: pushing $ORIG_IMG to $NEW_IMG..."
        if [[ "${DRYRUN}" == "yes" ]]; then
            continue
        fi
        docker pull $ORIG_IMG
        docker tag $ORIG_IMG $NEW_IMG
        docker push $NEW_IMG
        docker rmi $NEW_IMG $ORIG_IMG
    fi
done