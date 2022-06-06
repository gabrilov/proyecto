# Longhorn #

1. Agregar el repositorio.
```shell
helm repo add longhorn https://charts.longhorn.io
helm repo update
```
2. Instalar requerimientos en los nodos de almacenamiento
```shell
apt instal nfs-commmon
```
 
3. Sacar valores por defecto en la instalación
```shell
helm show values longhorn/longhorn > ./longhorn/longhorn-values.yaml
```
4. Cambiar el valor del servicio ui a load balancer e instalar con `helm`. Alternativamente se puede usar el archivo `longhorn-values.yaml` en esta carpeta:
```shell
helm install longhorn longhorn/longhorn --values longhorn-values.yaml -n longhorn-system --create-namespace
```

Para más detalles, consultar [la documentación de Longhorn](https://longhorn.io/docs/1.2.4/)