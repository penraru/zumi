#this program reads the serial port
#at a baud rate of 115200
#This code works with Linky

import serial

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 0.5
    )


def readSensors():
    #FrontLeft,FrontMiddle,FrontRight
    #SBottomLeft,SBottomRight
    #Battery Level
    #Mic level
    ser.write("L")
    read_serial = ser.readline()
    topLeft,topMiddle,topRight,bottomLeft,bottomRight,batterylvl, miclvl = read_serial.split(",")
    return int(topLeft),int(topMiddle),int(topRight),int(bottomLeft),int(bottomRight),float(batterylvl), int(miclvl)

#returns a tuple with the data as integers
def requestData():
    #ON linky only speed is currently requested

    ser.write("Z")#REQUEST INFO
    read_serial = ser.readline()
    #read the Serial line the rokit should be sending a message

    #chop up that message
    servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = read_serial.split(" ")
    #now return the data as integers
    return int(servo1Angle),int(servo2Angle),int(servoStep),int(speed),int(a19),int(a20),int(a21)

def requestObstacle():
    a = 0
    if(ser.readline() != ''):
        a = 1
    return a

def serialWait():
    return ser.inWaiting()
def victoryBeep():
    ser.write("J")

def forward():
    ser.write('M')

def stumble():
    ser.write('K')

def backward():
    ser.write('N')

def left():
    ser.write('O')

def right():
    ser.write('P')

def stop():
    ser.write('Q')


def speedDecrease():
    ser.write('V')

def speedIncrease():
    ser.write('W')


def speed(speedPercentage):

    servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = requestData()
    currentSpeed = speed

    while(currentSpeed > speedPercentage):
        servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = requestData()
        currentSpeed = speed
        speedDecrease()
    while(currentSpeed < speedPercentage):
        servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = requestData()
        currentSpeed = speed
        speedIncrease()

def setSpeed(speed):
    if speed < 0:
        speed = 0
    elif speed > 100:
        speed = 100
    j = speed % 10
    setModifier((speed - j) // 10)
    ser.write(b'l')
    setModifier(j)
    ser.write(b'm')

def setModifier(i):
    if i == 0:
        ser.write(b'a')
    elif i == 1:
        ser.write(b'b')
    elif i == 2:
        ser.write(b'c')
    elif i == 3:
        ser.write(b'd')
    elif i == 4:
        ser.write(b'e')
    elif i == 5:
        ser.write(b'f')
    elif i == 6:
        ser.write(b'g')
    elif i == 7:
        ser.write(b'h')
    elif i == 8:
        ser.write(b'i')
    elif i == 9:
        ser.write(b'j')
    else:
        ser.write(b'k')
