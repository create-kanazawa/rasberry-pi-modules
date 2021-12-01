#!/usr/bin/python
# coding: utf-8 

import time
import Adafruit_PCA9685
from func_servo import *

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

Vref = 3.297  # 電圧をテスターで実測する

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

if __name__ == '__main__':
        #print(OFFSETS[0][0])
        #data = readAdc(channel=0)
        #DS3218_J2(-90)
        #DS3218_J1(0)
        #DS3218_J0(0)
        #OPEN_hand()
        #time.sleep(1)
        #CLOSE_hand()
        #obj = detect_obj()
        #color = detect_color()
        #print(color)
        print("END.\n")