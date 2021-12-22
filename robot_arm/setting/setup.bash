#!/bin/bash
#########
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y  install expect
#########
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0
#########
sudo apt-get install -y python3-numpy
sudo apt-get install -y python3-setuptools
sudo apt-get install -y python3-pip
sudo pip install adafruit-pca9685
#########
#echo 'dtparam=i2c_baudrate=10000' | sudo tee -a /boot/config.txt>/dev/null
