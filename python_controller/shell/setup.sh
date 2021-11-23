SCRIPT_DIR=$(cd $(dirname $0); pwd)

#####FTPサーバ Vsftpd環境の作成
echo '-----------install vsftpd-----------'
sudo apt install vsftpd #FTPサーバのインストール
FTP_CONFIG_TRGET=/etc/vsftpd.conf
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
SHORTCUT_BASH=~/start_communication.bash
echo "cd "$SCRIPT_DIR>$SHORTCUT_BASH
echo "python3 processControlMain.py">>$SHORTCUT_BASH

#####pipでファイル管理モジュールwatchdogをインストール(python2.7はバージョン1.0.0以下を指定)
echo '-----------install watchdog-----------'
pip install watchdog==0.10.6

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
sudo chmod -R 777 $SCRIPT_DIR/../scripts/

######setup UDP port
sudo apt install ufw
sudo ufw allow 60000
sudo ufw allow 60001

######