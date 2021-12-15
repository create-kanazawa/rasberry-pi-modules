#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)

TIME=$(date)
echo "LOG is start from:"$TIME"-----------"

#sync git
echo 'waiting for git update...'
_IP=$(hostname -I) || true
wget -q --spider http://google.com
while [ $? -eq 0 ] 
do
  sleep 1
  wget -q --spider http://google.com
done

  _IP=$(hostname -I) || true
if [ "$_IP" ]; then
  echo $_IP
fi
git pull

#execute FTP
python3 $SCRIPT_DIR/../processControlMain.py
