1. Sacar valores por defecto en la instalación
```bash
helm show values longhorn/longhorn > ./longhorn/longhorn-values.yaml
```
2. Desplegar Longhorn
```bash
helm install longhorn longhorn/longhorn --namespace longhorn-system --create-namespace
```
3.
4. Cambiar el valor del servicio ui a load balancer y actualizar el despliegue:
```bash
helm upgrade --install longhorn longhorn/longhorn --values longhorn-values.yaml -n longhorn-system
```