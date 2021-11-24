#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd $SCRIPT_DIR/../
#sync git
echo 'waiting for git update...'
sleep 5
git pull
#execute FTP
python3 processControlMain.py
