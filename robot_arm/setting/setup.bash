#!/bin/bash
#########
sudo apt update
sudo apt upgrade
sudo apt -y  install expect
#########
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0
#########
sudo apt install -y python3-numpy
sudo apt install -y python3-setuptools
sudo apt install -y python3-pip
sudo pip3 install adafruit-pca9685
#########
#echo 'dtparam=i2c_baudrate=10000' | sudo tee -a /boot/config.txt>/dev/null
