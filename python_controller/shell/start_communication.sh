#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)

TIME=$(date)
echo "LOG is start from:"$TIME"-----------"

#sync git
echo 'waiting for git update...'
sleep 5
git pull

#execute FTP
python3 $SCRIPT_DIR/../processControlMain.py
