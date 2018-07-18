#All of the functions necessary to move Linky
import time
import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/src')
import Linky_SerialCom as ropi

speed = 30

def go_straight():
    ropi.setMotor(speed, speed)
    print(speed)

def turn_left():
    ropi.setMotor(speed, -speed)

def turn_right():
    ropi.setMotor(-speed, speed)

def stop():
    ropi.setMotor(0,0)

def set_speed(s):
    speed = s
