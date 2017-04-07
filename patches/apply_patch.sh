#!/bin/bash

OLD_DIR=$(pwd)

cp pause_button.diff /var/www
cd /var/www
patch -p1 --binary < pause_button.diff
cd $OLD_DIR

