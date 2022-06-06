# Ingress Controller y vista web #
## Nginx Ingress Controller ##

Seguir [la documentación de Nginx Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/) para instarlarlo. Alternativamente, ejecutar el siguiente comando:

```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.2.0/deploy/static/provider/cloud/deploy.yaml
```
## Despliegue de la vista web ##

Ejecutar los manifiestos en el orden en que aparecen. 

Se puede editar el nombre de dominio en `02-web-ingress.yaml`