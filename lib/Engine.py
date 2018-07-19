#All of the functions necessary to move Linky
import time
import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/src')
import Linky_SerialCom as ropi

speed = 30

# 7-19-18 These do not appear to be working. Linky is freaking out! 
def go_forward():
    time.sleep(2)
    ropi.setMotor(speed, speed)
    print("forward")

def stop():
    ropi.setMotor(0, 0)
    print("stop")

def go_backward():
    ropi.setMotor(-speed, -speed)
    print("backward")
    
def turn_left():
    ropi.setMotor(speed, -speed)
    print("left")

def turn_right():
    ropi.setMotor(-speed, speed)
    print("right")

def set_speed(s):
    speed = s
    print("speed = "+str(speed))
