#!/bin/bash

# Get all charts
mkdir -p data
helm list --all-namespaces | tail -n +2 | awk '{print $2, $1}' > data/helm-charts.txt

# helm get manifest -n d8-system ingress-nginx | yq -N eval '[.kind, .metadata.name] | join("/")' - | sort

# Take ns from file
function NS() {
    awk '{print $2}' data/helm-charts.txt
}
while read namespace name none;
    do echo $namespace/$name && \
       mkdir -p "data/$namespace/$name" && \
       helm get manifest -n $namespace $name > "data/$namespace/$name/$name.yaml" && \
       kubesplit -o "data/$namespace/$name" -i "data/$namespace/$name/$name.yaml";
done < data/helm-charts.txt
cd data
git add . 
git commit --allow-empty -m "$(date)"