#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)

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
git pull

#execute FTP
python3 $SCRIPT_DIR/../processControlMain.py
