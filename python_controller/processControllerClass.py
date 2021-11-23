#!/usr/bin/env python
# coding: utf-8
# 参考サイト
# https://bluebirdofoz.hatenablog.com/entry/2019/03/21/132515

# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

#サブプロセスを管理するsubprocessモジュールを追加
import subprocess as sp
from subprocess import PIPE

# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import time
import sys
import pigpio

# PatternMatchingEventHandler の継承クラスを作成
class ProcessHandlerByFTP(PatternMatchingEventHandler):
     #メンバ関数
     status_number = {"nutral":0,
        "wait_update":1,
        "wait_start":2,
        "on_execute":3,
        "emergency_stop":4}
     status =  1
     target_main = 'main.py'
     target_start = 'start.py'
     target_end = 'stop.py'
     target_reset = 'reset.py'
     proc = []

     # クラス初期化
     def __init__(self, patterns):
         super(ProcessHandlerByFTP, self).__init__(patterns=patterns)

     # ファイル作成時のイベント
     def on_created(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s created' % filename)

     # ファイル変更時のイベント
     def on_modified(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         self.action_by_status(filename)
         print('%s changed' % filename)

     # ファイル削除時のイベント
     def on_deleted(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s deleted' % filename)

     # ファイル移動時のイベント
     def on_moved(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s moved' % filename)

     def set_target(self,main,start,end):
         self.target_main = self.main
         self.target_start = self.start
         self.target_end = self.end

     def start_main_process(self):
         print("start the main process")
         self.proc = sp.Popen(['python3', 'scripts/'+self.target_main])
         print("subprocess ID:")

     def stop_main_process(self):
         try:
             self.proc.kill()
         except:
             print("")

     def reset_robot(self):
         self.proc = sp.Popen(['python3', 'scripts/'+self.target_end])
         #pi = pigpio.pi()
         #servo_pin1 = 18                      #thetaのモータGPIOピン設定
         #servo_pin2 = 19                      #th1のモータGPIOピン設定
         #servo_pin3 = 16                      #th2のモータGPIOピン設定
         #pi.set_mode(servo_pin1, pigpio.INPUT)
         #pi.set_mode(servo_pin2, pigpio.INPUT)
         #pi.set_mode(servo_pin3, pigpio.INPUT)
         #pi.stop()
         print("reset completed")

     def action_by_status(self,filename):
         print("-------------on action_by_status():-------------")
         #################when main script update#################
         if filename == self.target_main:#when main script update
             if self.status == self.status_number["wait_update"] or self.status == self.status_number["wait_start"] or self.status == self.status_number["emergency_stop"]:
                 print("transport status wait_start")
                 self.status = self.status_number["wait_start"]
             elif self.status == self.status_number["on_execute"]:
                 if self.proc.poll() != None:
                     print("transport status wait_start")
                     self.status = self.status_number["wait_start"]
                 else:
                     print("error: main process is still run. please wait or stop by command")
             else:
                 print("error: status number is",self.status)
         ##################when file "start" send##################
         elif filename == self.target_start:#when file "start" send
             if self.status == self.status_number["wait_start"]:
                 print("transport status on_execute")
                 self.status = self.status_number["on_execute"]
                 self.start_main_process()
             elif self.status == self.status_number["on_execute"]:
                 if self.proc.poll() != None:
                     print("transport status on_execute")
                     self.start_main_process()
                 else:
                     print("error: main process is still run. please wait or stop by command")
             else:
                 print("error: status number is",self.status)
         ##################when file "stop" send##################
         elif filename == self.target_end:#when file "stop" send
             if self.status == self.status_number["on_execute"] or self.status == self.status_number["wait_update"]:
                 print("transport status emergency_stop")
                 self.status = self.status_number["emergency_stop"]
                 self.stop_main_process()
                 self.reset_robot()
             else:
                 print("error: status number is",self.status)
#         elif filename == self.target_reset:#when file "reset" send
#             if self.status == self.status_number["emergency_stop"]:
#                 self.status = self.status_number["wait_update"]

         else:
             print("unexpected file ")



# コマンド実行の確認
if __name__ == "__main__":
     print("debug start")
     #このpythonファイルが存在するパスを取得する
     this_path = os.path.dirname(os.path.abspath(__file__))
     # this_path = "/var/www"
     print("this_path:",this_path)
     # 監視対象ディレクトリを指定する
     target_dir=this_path + "/scripts/"
     print(target_dir)
     # # 監視対象ファイルのパターンマッチを指定する
     target_file = '*.py'

     # ファイル監視の開始
     event_handler = ProcessHandlerByFTP([target_file])
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
