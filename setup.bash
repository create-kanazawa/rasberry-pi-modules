SCRIPT_DIR=$(cd $(dirname $0); pwd)
sudo bash $SCRIPT_DIR/python_controller/shell/setup.sh
sudo bash $SCRIPT_DIR/wheel_robot/setting/setup.bash
sudo bash $SCRIPT_DIR/robot_arm/setting/setup.bash
