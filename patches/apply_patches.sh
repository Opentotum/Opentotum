#!/bin/bash

OLD_DIR=$(pwd)

cp *.diff /var/www
cd /var/www

for f in *.diff; do
    patch -p1 --binary < $f
done

cd $OLD_DIR

