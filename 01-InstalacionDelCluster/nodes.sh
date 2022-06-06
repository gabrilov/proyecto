#!/bin/bash

# Envía comandos a todos los nodos
for i in {1..3}
do
    echo 
    echo "-----------------"
    echo "Enviado a m$i: $1"
    echo "-----------------"
    ssh m$i $1
    echo
    echo "-----------------"
    echo "Enviado a w$i: $1"
    echo "-----------------"
    ssh w$i $1
done
