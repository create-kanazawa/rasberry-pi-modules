#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)

TIME=$(date)
echo "LOG is start from:"$TIME"-----------"

#sync git
echo 'waiting for git update...'
sleep 5
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  echo $_IP
fi
git pull

#execute FTP
python3 $SCRIPT_DIR/../processControlMain.py
