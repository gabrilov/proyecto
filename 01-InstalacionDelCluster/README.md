# Instalación del clúster de K3s #

## Instalación de K3sup ##

Para instalar k3sup en el sistema hay que seguir las instrucciones descritas en el [repositorio de k3sup](https://github.com/alexellis/k3sup):

```shell
curl -sLS https://get.k3sup.dev | sh
sudo install k3sup /usr/local/bin/

k3sup --help
```

## Preparación de las conexiones SSH a los nodos ##

1. Configurar los alias como se desee en el archivo `alias-ssh`.
2. Agregar el contenido de `alias-ssh` al archivo `~/.ssh/config`.
```shell
cat alias-ssh >> ~/.ssh/config
```
3. Crear en cada nodo la contraseña para el usuario root.
```shell
sudo -i
passwd
```
4. Permitir en cada nodo el acceso root por ssh.
```shell
sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' \
/etc/ssh/sshd_config
```
4. Configurar las conexiones desatendidas a los nodos.
```shell
for i in {1..3} ; do ssh-copy-id m$i; done
for i in {1..3} ; do ssh-copy-id w$i; done
```
6. Se pueden usar los scripts para automatizar envíos de comandos a los nodos.
   
    * `nodes.sh` envía a todos los nodos.
    * `workers.sh` envía a los workers.
    * `masters.sh` envía a los maestros.
  
```shell
nodes.sh "comando-para-los-nodos"
``` 
## Instalación del clúster ##

1. Instalación del primer nodo.
```shell
k3sup install \
--host=192.168.122.10 \
--user=root \
--cluster \
--tls-san 192.168.122.1 \
--k3s-extra-args="--disable servicelb \
--disable local-storage \
--node-taint node-role.kubernetes.io/master=true:NoSchedule"
```
2. Instalación del resto de nodos maestros.
```shell
k3sup join \
--host=192.168.122.20 \
--server-user=root \
--server-host=192.168.122.10 \
--server \
--user=root \
--k3s-extra-args="--disable servicelb \
--disable local-storage \
--node-taint node-role.kubernetes.io/master=true:NoSchedule"
```
3. Instalación de los workers.
```shell
k3sup join \
--host=192.168.122.31 \
--server-user=root \
--server-host=192.168.122.10 \
--user=root
```
