#this program reads the serial port
#at a baud rate of 115200

import serial

ser = serial.Serial('/dev/ttyUSB0',115200)

#returns only 3 of 7 bottom IR sensors
def readBottomIRSensors():
    ser.write("L")
    read_serial = ser.readline()
    d11,d12,d13,d14,d16,d17,d18 = read_serial.split(" ")
    return int(d11),int(d14),int(d18)

#this request all the bottom IR sensors
def requestBottomIRSensors():
    ser.write("L")
    read_serial = ser.readline()
    d11,d12,d13,d14,d16,d17,d18 = read_serial.split(" ")
    return int(d11),int(d12),int(d13),int(d14),int(d16),int(d17),int(d18)

def requestIRmsg():
    #case 75:character "K"
    ser.write("K")
    irmsg = ser.readline()
    return int(irmsg)
    
def requestM1M2speed():
    #case 75:character "K"
    ser.write("u")
    read_serial = ser.readline()
    motor1speed, motor2speed = read_serial.split(" ")
    return int(motor1speed), int(motor2speed)

#returns a tuple with the data as integers
def requestData():
    ser.write("Z")#REQUEST INFO
    read_serial = ser.readline()
    #read the Serial line the rokit should be sending a message

    #chop up that message
    servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = read_serial.split(" ")
    #now return the data as integers
    return int(servo1Angle),int(servo2Angle),int(servoStep),int(speed),int(a19),int(a20),int(a21)    


#returns a tuple with the data as integers
def readTopIRsensors():
    servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = requestData()
    #now return the strings as integers
    #A19 is analog pin 19 which on the rokit smartinventor board is 
    return int(a19),int(a20),int(a21)    

def forward():
    ser.write('M')

def backward():
    ser.write('N')

def left():
    ser.write('O')

def right():
    ser.write('P')
    
def stop():
    ser.write('Q')

def servo1Decrease():
    ser.write('R')

def servo1Increase():
    ser.write('S')

def servo2Decrease():
    ser.write('T')

def servo2Increase():
    ser.write('U')

def speedDecrease():
    ser.write('V')

def speedIncrease():
    ser.write('W')

def servoStepIncrease():
    ser.write('X')

def servoStepDecrease():
    ser.write('Y')

def motor1increase():
    ser.write('q')
    
def motor1decrease():
    ser.write('r')

def motor2increase():
    ser.write('s')
    
def motor2decrease():
    ser.write('t')

def setM1Speed(speedPercentage):
    m1speed, m2speed = requestM1M2speed()
    currentSpeed = m1speed
    while(currentSpeed < speedPercentage):
        m1speed, m2speed = requestM1M2speed()
        currentSpeed = m1speed
        motor1increase()
    while(currentSpeed > speedPercentage):
        m1speed, m2speed = requestM1M2speed()
        currentSpeed = m1speed
        motor1decrease()
    
def setM2Speed(speedPercentage):
    m1speed, m2speed = requestM1M2speed()
    currentSpeed = m2speed
    while(currentSpeed < speedPercentage):
        m1speed, m2speed = requestM1M2speed()
        currentSpeed = m2speed
        motor2increase()
    while(currentSpeed > speedPercentage):
        m1speed, m2speed = requestM1M2speed()
        currentSpeed = m2speed
        motor2decrease()    


def speed(speedPercentage):
    
    servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = requestData()
    currentSpeed = speed
    
    while(currentSpeed > speedPercentage):
        servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = requestData()
        currentSpeed = speed
        #print(currentSpeed)
        speedDecrease()
    while(currentSpeed < speedPercentage):
        servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = requestData()
        currentSpeed = speed
        #print(currentSpeed)
        speedIncrease()
    
    




