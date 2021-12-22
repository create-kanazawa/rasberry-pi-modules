SCRIPT_DIR=$(cd $(dirname $0); pwd)
######apt update upgrade######
sudo apt update
sudo apt upgrade
bash $SCRIPT_DIR/python_controller/shell/setup.sh
bash $SCRIPT_DIR/wheel_robot/setting/setup.bash
bash $SCRIPT_DIR/robot_arm/setting/setup.bash
