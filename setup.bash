SCRIPT_DIR=$(cd $(dirname $0); pwd)
######apt update upgrade######
sudo apt update -y
sudo apt upgrade -y

######setting i2c spi######
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0

######install module######
sudo apt install -y expect
sudo apt install -y python3-numpy
sudo apt install -y python3-setuptools
sudo apt install -y python3-pip
sudo pip3 install adafruit-pca9685
#########
bash $SCRIPT_DIR/python_controller/shell/setup.sh
bash $SCRIPT_DIR/wheel_robot/setting/setup.bash
bash $SCRIPT_DIR/robot_arm/setting/setup.bash
