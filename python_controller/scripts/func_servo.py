#!/usr/bin/python
# coding: utf-8 

from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

OFFSETS = [[164,217],[163,220],[160,219]]

def DS3218_J0( ang ):
        
        channel = 0
        ang=ang+90
        PtoD = round((OFFSETS[0][0]/90)*ang + OFFSETS[0][1])
        pwm.set_pwm(channel, 0, PtoD)

def DS3218_J1( ang ):
        
        channel = 1
        ang=ang+90
        PtoD = round((OFFSETS[1][0]/90)*ang + OFFSETS[1][1])
        pwm.set_pwm(channel, 0, PtoD)

def DS3218_J2( ang ):
        
        channel = 2
        ang=ang+90
        PtoD = round((OFFSETS[2][0]/90)*ang + OFFSETS[2][1])
        pwm.set_pwm(channel, 0, PtoD)
        
def MG90S( ang ):
        #mada
        channel = 4
        PtoD = round((650-150)/180*ang + 150)
        pwm.set_pwm(channel, 0, PtoD)

def OPEN_hand():
        MG90S(0)
        
def CLOSE_hand():
        MG90S(55)
