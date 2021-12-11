#!/bin/bash
#########
sudo sh -c 'echo 127.0.1.1 $(hostname) >> /etc/hosts'
#
echo 'please input IP address (ex. 192.168.100.***)'
#
read str
#
echo 'IP address is set to '$str
#
TARGET_CONF=/etc/dhcpcd.conf
#if [ ! -e $TARGET_CONF'-default' ];then
#	sudo cp $TARGET_CONF $TARGET_CONF'-default'
#fi
TIME=$(date)
echo "#-----------change by setup.bash: "$TIME"-----------">>$FTP_CONFIG_TRGET
sudo echo 'interface wlan0'>>$TARGET_CONF
#sudo echo 'static ip_address='$ip'/24'>>$TARGET_CONF
sudo echo 'static ip_address=192.168.100.140/24'>>$TARGET_CONF
sudo echo 'static routers=192.168.100.1'>>$TARGET_CONF
sudo echo 'static domain_name_servers=192.168.100.1'>>$TARGET_CONF
#########
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0
#########
sudo raspi-config nonint do_hostname steam-lab-99
#########
sudo apt-get install python3-numpy
sudo apt-get install python3-setuptools
sudo apt-get install python3-pip
sudo apt-get install python3-pip
sudo apt-get install git git-core
sudo pip install adafruit-pca9685
#########
echo 'dtparam=i2c_baudrate=10000' | sudo tee -a /boot/config.txt>/dev/null
