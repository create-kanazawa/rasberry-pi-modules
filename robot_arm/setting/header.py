#-----------------------robot_arm header-----------------------
import time
import math
import sys
import numpy as np

import Adafruit_PCA9685
#from func_servo import *

################### robot #######################
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)


CURRENT_TH = [1,1,1]
DH = 1 #最高速度
DELTA_TIME = 0.01 #最高速度の時の待ち時間

#arm length
L = [110.3, 95]
freq = 50

def servo_angle(angle1, angle2, angle3):
    delta_th = [0]*3
    delta_th[0] = angle1 - CURRENT_TH[0]
    delta_th[1] = angle2 - CURRENT_TH[1]
    delta_th[2] = angle3 - CURRENT_TH[2]
    delta_th_max = max(abs(delta_th[0]),abs(delta_th[1]),abs(delta_th[2]));
    n = int(delta_th_max / DH)
    if (delta_th_max != 0):
        for i in range(n):
            servo1(abs(DH*delta_th[0]/delta_th_max), delta_th[0])
            servo2(abs(DH*delta_th[1]/delta_th_max), delta_th[1])
            servo3(abs(DH*delta_th[2]/delta_th_max), delta_th[2])
        
def servo1(dh, delta_th):
    CURRENT_TH[0] += np.sign(delta_th) * dh
    
    channel = 0
    ang=CURRENT_TH[0]+90
    PtoD = int(round((OFFSETS[channel][0]/90)*ang + OFFSETS[channel][1]))
    pwm.set_pwm(channel, 0, PtoD)
    
    time.sleep(abs(DELTA_TIME*dh/DH))
    print(CURRENT_TH)
    
def servo2(dh, delta_th):
    CURRENT_TH[1] += np.sign(delta_th) * dh
    
    channel = 1
    ang=CURRENT_TH[1]+90
    PtoD = int(round((OFFSETS[channel][0]/90)*ang + OFFSETS[channel][1]))
    pwm.set_pwm(channel, 0, PtoD)
    
    time.sleep(abs(DELTA_TIME*dh/DH))
    print(CURRENT_TH)
    
def servo3(dh, delta_th):
    CURRENT_TH[2] += np.sign(delta_th) * dh
    
    channel = 2
    ang=-CURRENT_TH[2]+90
    PtoD = int(round((OFFSETS[channel][0]/90)*ang + OFFSETS[channel][1]))
    pwm.set_pwm(channel, 0, PtoD)
    
    time.sleep(abs(DELTA_TIME*dh/DH))
    print(CURRENT_TH)

def servo_angle1(angle):
    servo_angle(angle, CURRENT_TH[1], CURRENT_TH[2])
    
def servo_angle2(angle):
    servo_angle(CURRENT_TH[0], angle, CURRENT_TH[2])
    
def servo_angle3(angle):
    servo_angle(CURRENT_TH[0], CURRENT_TH[1], angle)
        
#逆運動学計算
def IK(X,Y,Z):
    servo_angle(X,Y,Z)
        
# 順運動学の計算
def fk(th):
    # 各リンクの長さと関節角度の取得
    l1, l2 = L
    th1, th2,t = th

    # リンク1の手先
    x1 = l1 * math.cos(th1)
    y1 = l1 * math.sin(th1)

    # リンク2の手先
    x2 = x1 + l2 * math.cos(th1 + th2)
    y2 = y1 + l2 * math.sin(th1 + th2)

    # 手先位置をNumPy配列に格納して返す
    return [x2 , y2]

#degreeに変換
def conv_deg(th, X):
    th1 ,th2 ,t= th
    th1_deg = np.sign(X)*(180/math.pi*th1 -90)    #根元のアーム角度
    th2_deg = np.sign(X)*(-(180/math.pi*th2))    #手先のアーム角度
    th_deg  = 180/math.pi*t
    return [th1_deg , th2_deg , th_deg]

def initial_servo():
    servo_angle(0,0,0)
    
################ gripper ################


import time
import spidev

L_MAX = 510
OFF_SET = 360
R_MIN = 210

Vref = 3.297  # 電圧をテスターで実測する

spi = spidev.SpiDev()

spi.open(0, 0)  # bus0,cs0
spi.max_speed_hz = 100000  # 100kHz 必ず指定する
        
def readAdc(channel):
        adc = spi.xfer2([1, (8 + channel) << 4, 200])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

def detect_obj():
    obj = 0
    
    for i in range(10):
        data = readAdc(channel=0)
        volts = (data * Vref) / float(1023)
        
        if(volts > 0.1):#white
            a = 1
            obj += a
        print(obj)
        time.sleep(0.01)
    
    if(obj > 5):
        obj = 1#exist obj
    else:
        obj = 0#nothing
    return obj

def detect_color():
    col = ""
    val = 0
    for i in range(10):
        data = readAdc(channel=0)
        volts = (data * Vref) / float(1023)
        
        val += volts
        print(val)
        time.sleep(0.01)
    
    ave = val / 10
    if 0.15 < ave < 0.3:
        col = "black"#black
    
    elif 0.4 < ave < 0.5:
        col = "plane"#sponji
        
    elif 0.6 < ave < 1:
        col = "white"#white
        
    return col

initial_servo()
OPEN_hand()
