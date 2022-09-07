#!/bin/bash

# Get all charts
#helm list --all-namespaces > data/helm-charts.txt

# Take ns from file
function NS() {
    awk '{print $2}' data/helm-charts.txt
}
while read name namespace trio;
    do mkdir -p "data/$namespace/$name";
done <data/helm-charts.txt