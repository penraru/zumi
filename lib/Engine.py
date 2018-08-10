#Import this file to use all of the functions necessary to move Linky
import time
import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/src')
import Linky_SerialCom as ropi

speed = 30

#[TODO: add parameters in each method to specify how long]

time.sleep(2)

def go_forward():
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
    global speed
    speed = s
    print("speed = "+str(speed))
