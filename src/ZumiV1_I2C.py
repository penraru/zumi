#this program reads the serial port
#at a baud rate of 115200
#This code works with Linky

import smbus

bus = smbus.SMBus(1)
address = 0x04
term = 126

def forward():
    bus.write_i2c_block_data(address, 0, [77, term])

def backward():
    bus.write_i2c_block_data(address, 0, [78, term])

def left():
    bus.write_i2c_block_data(address, 0, [79, term])

def right():
    bus.write_i2c_block_data(address, 0, [80, term])
    
def stop():
    bus.write_i2c_block_data(address, 0, [81, term])

def speedDecrease():
    bus.write_i2c_block_data(address, 0, [86, term])

def speedIncrease():
    bus.write_i2c_block_data(address, 0, [87, term])

def setMotor(i, j):
    """Sets the individual speed of each motor.
    Args: 2 integers, from -100 to 100, for the left and right motors, respectively.
    """
    if i<0:
        i=-i
        if j<0:
            a = 67
            j=-j
        else:
            a = 66
    else:
        if j<0:
            a = 65
            j=-j
        else:
            a = 64
    if i>100:
        i = 100
    if j>100:
        j = 100
    bus.write_i2c_block_data(address, 0, [a, i, j, term])
