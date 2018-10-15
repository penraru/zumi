#Import this file to use all of the functions necessary to move Linky
import time
import sys
sys.path.insert(0,'/home/pi/zumi/src')
import Linky_SerialCom as ropi

#[TODO: add parameters in each method to specify how long]

def go_forward():
    ropi.forward()
    print("forward")

def stop():
    ropi.stop()
    print("stop")

def go_backward():
    ropi.backward()
    print("backward")
    
def turn_left():
    ropi.turnDegrees(-90)
    print("left")

def turn_right():
    ropi.turnDegrees(90)
    print("right")
    
def right_a_bit():
    ropi.setMotor(10, -5)
    time.sleep(.1)
    ropi.stop()
    
def left_a_bit():
    ropi.setMotor(-5, 10)
    time.sleep(.1)
    ropi.stop()
    
def forward_a_bit():
    ropi.setMotor(20, 20)
    time.sleep(.3)
    ropi.stop()

def set_speed(s):
    ropi.setSpeed(s)
    print("speed = "+str(s))

def start_line_follower():
    ropi.lineTracer()

def keep_turning_left():
    ropi.left()

def keep_turning_right():
    ropi.right()
