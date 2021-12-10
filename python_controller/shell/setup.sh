SCRIPT_DIR=$(cd $(dirname $0); pwd)

#####FTPサーバ Vsftpd環境の作成
echo '-----------install vsftpd-----------'
sudo apt install vsftpd #FTPサーバのインストール
FTP_CONFIG_TRGET=/etc/vsftpd.conf
if [ ! -e $FTP_CONFIG_TRGET'-default' ];then
	sudo cp $FTP_CONFIG_TRGET $FTP_CONFIG_TRGET'-default'
fi
TIME=$(date)
echo "#-----------change by setup.bash: "$TIME"-----------" | sudo tee -a $FTP_CONFIG_TRGET>/dev/null
echo 'local_enable=YES' | sudo tee -a $FTP_CONFIG_TRGET>/dev/null
echo 'write_enable=YES' | sudo tee -a $FTP_CONFIG_TRGET>/dev/null
echo 'local_umask=022' | sudo tee -a $FTP_CONFIG_TRGET>/dev/null
echo 'ascii_upload_enable=YES' | sudo tee -a $FTP_CONFIG_TRGET>/dev/null
echo 'ascii_download_enable=YES' | sudo tee -a $FTP_CONFIG_TRGET>/dev/null
cat $FTP_CONFIG_TRGET
sudo service vsftpd start #FTPサーバの再起動

#####ショートカット用bashファイルの作成
#echo '-----------install vsftpd-----------'
#SHORTCUT_BASH=~/start_communication.bash
#echo "cd "$SCRIPT_DIR>$SHORTCUT_BASH
#echo "python3 processControlMain.py">>$SHORTCUT_BASH

#####pipでファイル管理モジュールwatchdogをインストール(python2.7はバージョン1.0.0以下を指定)
echo '-----------install watchdog-----------'
sudo apt-get install python-pip
sudo apt-get install python-pip3
pip install watchdog==0.10.6
pip3 install watchdog

######PHP server setup
#sudo apt update
#sudo apt install apache2 -y
#sudo apt install php libapache2-mod-php -y
#sudo apt install apache2 -y
#sudo service apache2 start

######move default file to /var/www/scripts/
#PYTHON_FOLDER=scripts
#cd /var/www/
#mkdir $PYTHON_FOLDER
#cp $SCRIPT_DIR/../php/file_upload.php ./
#cp $SCRIPT_DIR/../html/send_form.html ./
#cp $SCRIPT_DIR/../scripts/main.py ./$PYTHON_FOLDER
#cp $SCRIPT_DIR/../scripts/start.py ./$PYTHON_FOLDER
#cp $SCRIPT_DIR/../scripts/stop.py ./$PYTHON_FOLDER
#cp $SCRIPT_DIR/../scripts/reset.py ./$PYTHON_FOLDER

######set chmod of /var/www/
#sudo chmod -R 777 /var/www/

######set chmod of scripts/
echo '-----------set chmod to scripts/-----------'
sudo chmod 777 $SCRIPT_DIR/start_communication.sh
sudo chmod -R 777 $SCRIPT_DIR/../scripts/

######setup UDP port
echo '-----------setup UDP port-----------'
sudo apt install ufw
#sudo ufw allow 22
#sudo ufw allow 21
#sudo ufw allow 60000
#sudo ufw allow 60001
sudo ufw allow from 192.168.100.0/24
sudo ufw enable
sudo ufw reload

######set autostart file
echo '-----------setup auto start file-----------'
TARGET_SHELL=start_communication.sh
### auto start setup CUI version
command=$SCRIPT_DIR/$TARGET_SHELL'&>'$SCRIPT_DIR/../output.log
sudo echo $command | sudo tee -a /etc/rc.local>/dev/null

###auto start setup for GUI version
#FTP_START_TARGET=ftp_start.desktop
#FTP_START_DIR=~/.config/autostart
#if [ ! -d $FTP_START_DIR ];then
#	mkdir $FTP_START_DIR 
#	cd $_
#	touch $FTP_START_TARGET
#	echo '[Desktop Entry]' | sudo tee -a $FTP_START_TARGET>/dev/null
#	echo 'Exec=lxterminal -e '$SCRIPT_DIR'/../shell/'$TARGET_SHELL | sudo tee -a $FTP_START_TARGET>/dev/null
#	echo 'Type=Application' | sudo tee -a $FTP_START_TARGET>/dev/null
#	echo 'Name=FTP_server' | sudo tee -a $FTP_START_TARGET>/dev/null
#	echo 'Terminal=true' | sudo tee -a $FTP_START_TARGET>/dev/null
#fi

######set up this robot
echo '-----------setup header file for robot-----------'
echo 'please select this header folder...'
cd ${SCRIPT_DIR}/../
select VAR in exit robot_arm wheel_robot
do 
	echo 'your selected item is '$VAR
	if [ $VAR = 'exit' ];then
		break
	else
		echo -n $VAR>>temp.txt
	fi
done


echo 'complete the set up proccess'

