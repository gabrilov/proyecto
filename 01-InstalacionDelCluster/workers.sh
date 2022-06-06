#!/bin/bash

for i in {1..3}
do
    echo
    echo "-----------------"
    echo "Enviado a w$i: $1"
    echo "-----------------"
    ssh w$i $1
done
