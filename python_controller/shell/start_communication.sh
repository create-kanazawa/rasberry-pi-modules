#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)
expect_message_key_password="Enter passphrase for key '/home/pi/.ssh/id_rsa': "
password="robotics"

TIME=$(date)
echo "LOG is start from:"$TIME"-----------"

#sync git
echo 'waiting for git update...'
_IP=$(hostname -I) || true
wget -q --spider https://github.com
while [ $? -ne 0 ] 
do
  sleep 1
  wget -q --spider https://github.com
done

 _IP=$(hostname -I) || true
if [ "$_IP" ]; then
  echo $_IP
fi
cd ${SCRIPT_DIR}/../
expect -c "
        set timeout 2
        spawn git pull
        expect \"${expect_message_key_password}\"
        send \"${password}\n\"
        interact
"
#execute FTP
python3 $SCRIPT_DIR/../processControlMain.py
