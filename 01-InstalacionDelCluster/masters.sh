#!/bin/bash

for i in {1..3}
do
    echo 
    echo "-----------------"
    echo "Enviado a m$i: $1"
    echo "-----------------"
    ssh m$i $1
done
