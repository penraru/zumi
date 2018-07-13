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
        #print(currentSpeed)
        speedDecrease()
    while(currentSpeed < speedPercentage):
        servo1Angle,servo2Angle,servoStep,speed,a19,a20,a21 = requestData()
        currentSpeed = speed
        #print(currentSpeed)
        speedIncrease()
    
def setSpeed(i):
    if i < 0:
        i = 0
    if i > 100:
        i = 100
    j = i%10
    setModifier((i-j)/10)
    ser.write('l')
    setModifier(j)
    ser.write('m')

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

def flush():
    ser.flushInput()

def requestObstacle():
    a = 0
    if ser.inWaiting():
        a = 1
    return a

def followLine():
    ser.write('K')

def setTurnBias(a):
    if a == 0:
        setModifier(0)
    else:
        setModifier(1)
    ser.write('R')

def setMotor(i, j):
    """Sets the individual speed of each motor.
    Args: 2 integers, from -100 to 100, for the left and right motors, respectively.
    """
    reverse1 = 0
    reverse2 = 0
    if i < -100:
        i = -100
    if i < 0:
        i *= -1
        reverse1 = 1
    if i > 100:
        i = 100
    if j < -100:
        j = -100
    if j < 0:
        j *= -1
        reverse2 = 2
    if j > 100:
        j = 100
    k = i % 10
    setModifier((i - k) // 10)
    ser.write(b'q')
    setModifier(k)
    ser.write(b'r')
    k = j % 10
    setModifier((j - k) // 10)
    ser.write(b's')
    setModifier(k)
    ser.write(b't')
    setModifier(reverse1 + reverse2)
    ser.write(b'u')
