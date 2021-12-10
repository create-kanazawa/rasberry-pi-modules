#!/usr/bin/env python
# coding: utf-8
import sys
import os
import socket

this_path = os.path.dirname(__file__)
sys.path.append(this_path)
from processControllerClass import *

if __name__ == "__main__":
     print("FTP communication start...")
     #show the IP address
     #host = socket.gethostname()
     #ip = socket.gethostbyname(host)
     #print("This IP address:",ip)
     #このpythonファイルが存在するパスを取得する
     this_path = os.path.dirname(os.path.abspath(__file__))
     # this_path = "/var/www"
     # 監視対象ディレクトリを指定する
     target_dir=this_path + "/scripts/"
     print("waiting path for FTP is :",target_dir)
     #print(target_dir)
     # # 監視対象ファイルのパターンマッチを指定する
     target_file = '*.py'
     # ファイル監視の開始
     event_handler = ProcessHandlerByFTP([target_file])
     event_handler.path=target_dir
     observer = Observer()
     observer.schedule(event_handler, target_dir, recursive=True)
     observer.start()
     # 処理が終了しないようスリープを挟んで無限ループ
     try:
         while True:
             time.sleep(0.1)
     except KeyboardInterrupt:
         observer.stop()
     observer.join()
