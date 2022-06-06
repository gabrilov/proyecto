#!/bin/bash

helm repo add longhorn https://charts.longhorn.io
helm repo update
helm install longhorn longhorn/longhorn --values longhorn-values.yaml -n longhorn-system --create-namespace