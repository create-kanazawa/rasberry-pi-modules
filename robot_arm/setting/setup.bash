#!/bin/bash
#########固定IPアドレスの設定を行う
sudo sh -c 'echo 127.0.1.1 $(hostname) >> /etc/hosts'
#端末からIPアドレスを指定する
echo 'please input IP address (ex: 192.168.100.***):' 
#入力を受付、その入力を「str」に代入
read ip 
#結果を表示
echo 'IP address is set to '$ip
#設定ファイルに書き込みする
TARGET_CONF=/etc/dhcpcd.conf
if [ ! -e $TARGET_CONF'-default' ];then
	sudo cp $TARGET_CONF $TARGET_CONF'-default'
fi
TIME=$(date)
echo "#-----------change by setup.bash: "$TIME"-----------">>$FTP_CONFIG_TRGET
sudo echo 'interface wlan0'>>$TARGET_CONF
sudo echo 'static ip_address='$ip'/24'>>$TARGET_CONF
sudo echo 'static routers=192.168.100.1'>>$TARGET_CONF
sudo echo 'static domain_name_servers=192.168.100.1'>>$TARGET_CONF

#########I2C通信の設定
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0

#########ホストネームの変更
sudo raspi-config nonint do_hostname steam-lab-99

#########モジュールのインストール
sudo apt-get -y install　python3-numpy
sudo apt-get -y install　python3-setuptools
sudo apt-get -y install　python3-pip
sudo apt-get -y install　python3-pip
sudo apt-get -y install git git-core
sudo pip -y install adafruit-pca9685

#########I2C通信の設定を通信速度を設定する
echo 'dtparam=i2c_baudrate=10000' | sudo tee -a /boot/config.txt>/dev/null

#########GPIOの設定(今は不要)
#sudo apt install pigpio python-pigpio python3-
