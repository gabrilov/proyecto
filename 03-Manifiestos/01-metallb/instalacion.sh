#!/bin/bash

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/namespace.yaml
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/metallb.yaml

echo "----------------------------------------"
echo "Script finalizado"
echo "configura el pool de IP en el config map"
echo "----------------------------------------"
