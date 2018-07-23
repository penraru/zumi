import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/src')
import Linky_SerialCom as linky

def get_front_distance():
    topLeft, topMiddle, topRight, bottomLeft, bottomRight, batterylvl, miclvl = linky.readSensors()
    return topMiddle

def get_left_distance():
    topLeft, topMiddle, topRight, bottomLeft, bottomRight, batterylvl, miclvl = linky.readSensors()
    return topLeft

def get_right_distance():
    topLeft, topMiddle, topRight, bottomLeft, bottomRight, batterylvl, miclvl = linky.readSensors()
    return topRight