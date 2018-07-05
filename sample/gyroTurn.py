#!/usr/bin/python
import smbus
import math
import time
import os
import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/src')
import Linky_SerialCom as ropi
 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

# Initialize constants
GYRO_SAMPLERATE = 100
 
# Initialize variables
millis = int(round(time.time()*1000))
angle = 0.0
angleNew = 0.0


bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect
 

def read_byte(reg):
	return bus.read_byte_data(address, reg)
 
def read_word(reg):
	h = bus.read_byte_data(address, reg)
	l = bus.read_byte_data(address, reg+1)
	value = (h << 8) + l
	return value
 
def read_word_2c(reg):
	val = read_word(reg)
	if (val >= 0x8000):
		return -((65535 - val) + 1)
	else:
		return val
	    
def get_orientation(millis,angle,angleNew):
    
    if int(round(time.time()*1000)) - millis >= GYRO_SAMPLERATE:
        gyroscope_zout = read_word_2c(0x47)
        gyroscope_zout_scaled = gyroscope_zout / 131
        if abs(gyroscope_zout_scaled) > 5:
            angleNew = gyroscope_zout_scaled * GYRO_SAMPLERATE/1000 *0.98
            if angleNew > 0:
                angleNew *= 90/80.0
            else:
                angleNew *= 90/100.0
            angle+=angleNew
        millis = int(round(time.time()*1000))
    return angle


bus.write_byte_data(address, power_mgmt_1, 0)
 
gyroscope_zout = read_word_2c(0x47)
 
gyroscope_zout_scaled = gyroscope_zout / 131


        
print "Getting ready to turn..."
time.sleep(2)#Need sleep before turning for some weird reason?
ropi.left()
time.sleep(.5)

while angle < 90:      
        angle = get_orientation(millis,angle,angleNew)
      
ropi.stop()
print "stopped after " + str(angle) + " degrees"
