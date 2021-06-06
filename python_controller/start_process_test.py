#!/usr/bin/env python
# coding: utf-8

# dateコマンドを実行して文字列として結果を得る
import time
import subprocess as sp
from subprocess import PIPE


print("------------start.py------------")
proc = sp.Popen(['python', 'scripts/main.py'])
time.sleep(5)
print("stop the process")
proc.poll()
proc.kill()
print("------------end------------")
