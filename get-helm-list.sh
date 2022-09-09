#!/bin/bash

# Get all charts
#helm list --all-namespaces > data/helm-charts.txt

# helm get manifest -n d8-system ingress-nginx | yq -N eval '[.kind, .metadata.name] | join("/")' - | sort

# Take ns from file
function NS() {
    awk '{print $2}' data/helm-charts.txt
}
while read name namespace none;
    do echo $namespace/$name && \
       mkdir -p "data/$namespace/$name" && \
       helm get manifest -n $namespace $name > "data/$namespace/$name/";
done <data/helm-charts.txt