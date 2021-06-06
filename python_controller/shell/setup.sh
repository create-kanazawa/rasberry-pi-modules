SCRIPT_DIR=$(cd $(dirname $0); pwd)

#FTPサーバ Vsftpd環境の作成
sudo apt install vsftpd　
sudo service vsftpd start

# pipでファイル管理モジュールwatchdogをインストール(python2.7はバージョン1.0.0以下を指定)
pip install watchdog==0.10.6

#PHP server setup
sudo apt update
sudo apt install apache2 -y
sudo apt install php libapache2-mod-php -y
sudo apt install apache2 -y
sudo service apache2 start

#move default file to /var/www/scripts/
PYTHON_FOLDER=scripts
cd /var/www/
mkdir $PYTHON_FOLDER
cp $SCRIPT_DIR/../php/file_upload.php ./
cp $SCRIPT_DIR/../html/send_form.html ./
cp $SCRIPT_DIR/../scripts/main.py ./$PYTHON_FOLDER
cp $SCRIPT_DIR/../scripts/start.py ./$PYTHON_FOLDER
cp $SCRIPT_DIR/../scripts/stop.py ./$PYTHON_FOLDER
cp $SCRIPT_DIR/../scripts/reset.py ./$PYTHON_FOLDER

# set chmod of /var/www/
sudo chmod -R 777 /var/www/
