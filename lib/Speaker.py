#Import this file to use all of Zumi's sound functions
import sys
sys.path.insert(0,'/home/pi/zumi/src')
import Linky_SerialCom as zumi

def play_sad_sound():
    zumi.beepSad()

def play_happy_sound():
    zumi.beepHappy()
