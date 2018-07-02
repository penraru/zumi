import os
import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/src')
import Linky_SerialCom as ropi

sys.path.append('/usr/local/lib/python2.7/site-packages')

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

#Initialize constants
RESOLUTION_W = 128
RESOLUTION_H = 96

#Initialize variables
chicMat = np.zeros([6,3])
myX = 0
myY = 0
targetX = 0
targetY = 0
bearing = 0
bearingTemp = 0
obstruction = 0
interIter = 0
instructions = []
camera = PiCamera()
camera.resolution = (RESOLUTION_W, RESOLUTION_H)
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera)
time.sleep(2)

def printInstructions():
    i = 0
    for i in range(0,len(instructions)):
        print(instructions[i])

def turnLeft(a):
    time.sleep(a)
    ropi.stop()
    ropi.left()
    time.sleep(0.2)
    ropi.stop()
    ropi.stumble()
    time.sleep(0.7)
    ropi.stop()
    ropi.setTurnBias(0)

def turnRight(a):
    print(a)
    time.sleep(a)
    ropi.stop()
    ropi.right()
    time.sleep(0.2)
    ropi.stop()
    ropi.stumble()
    time.sleep(0.7)
    ropi.stop()
    ropi.setTurnBias(1)
    
def instructionsAppend(b):
    global bearingTemp
    a = b - bearingTemp
    if(a == -3):
        a+=4
    elif(a == 3):
        a-=4
    instructions.append(a)
    bearingTemp = b

def calcMat(sX,sY,eX,eY,m=[]):
    global obstruction
    global interIter
    global bearingTemp
    del instructions[:]
    interIter = 1
    i = sX
    j = sY
    bearingTemp = bearing
    #If there is a horizontal obstruction, switch rows. If there is a vertical obstruction, switch columns
    if(obstruction == 1):
        #Obstruction detected when moving vertical. Switch columns
        if(bearingTemp%2 == 1):
            if(i%2 == 1):
                instructionsAppend(2)   #\
                m[i,j] = 2              # Would be nice if these lines could be made into a function
                i-=1                    #/
            else:
                instructionsAppend(0)
                m[i,j] = 0
                i+=1
        #Obstruction detected when moving horizontal. Move to top or bottom row
        if(bearingTemp%2 == 0): #Do NOT switch to else or elif
            if(j == 0):
                while(j < 2):
                    instructionsAppend(3)
                    m[i,j] = 3
                    j+=1
            elif(j == 2):
                instructionsAppend(1)
                m[i,j] = 1
                j-=1
        obstruction = 0
    #If routing from a center node, move to the top or bottom
    if(j == 1):
        if(eY == 2):
            instructionsAppend(3)
            m[i,j] = 3
            j+=1
        else:
            instructionsAppend(1)
            m[i,j] = 1
            j-=1
    #Travel along X direction
    while(i < eX):
        instructionsAppend(0)
        m[i,j] = 0
        i+=1
    while(i > eX):
        instructionsAppend(2)
        m[i,j] = 2
        i-=1
    #Travel along Y direction
    while(j < eY):
        instructionsAppend(3)
        m[i,j] = 3
        j+=1
    while(j > eY):
        instructionsAppend(1)
        m[i,j] = 1
        j-=1
    instructions.append(3)
    printInstructions()

def updateBearing(x):
    global myX
    global myY
    global bearing
    bearing += x
    if bearing < 0:
        bearing += 4
    if bearing > 3:
        bearing -=4
    if bearing == 0:
        myX += 1
    elif bearing == 1:
        myY -= 1
    elif bearing == 2:
        myX -= 1
    else:
        myY += 1

#Initialize
while 1:
    command = raw_input("Please enter starting X-coordinate: ")
    if command == "0":
        myX = 0
        break
    elif command == "1":
        myX = 1
        break
    elif command == "2":
        myX = 2
        break
    elif command == "3":
        myX = 3
        break
    elif command == "4":
        myX = 4
        break
    elif command == "5":
        myX = 5
        break
    print("Invalid input!")
while 1:
    command = raw_input("Please enter starting Y-coordinate: ")
    if command == "0":
        myY = 0
        break
    elif command == "1":
        myY = 1
        break
    elif command == "2":
        myY = 2
        break
    print("Invalid input!")
while 1:
    command = raw_input("Please enter target X-coordinate: ")
    if command == "0":
        targetX = 0
        break
    elif command == "1":
        targetX = 1
        break
    elif command == "2":
        targetX = 2
        break
    elif command == "3":
        targetX = 3
        break
    elif command == "4":
        targetX = 4
        break
    elif command == "5":
        targetX = 5
        break
    print("Invalid input!")
while 1:
    command = raw_input("Please enter target Y-coordinate: ")
    if command == "0":
        targetY = 0
        break
    elif command == "1":
        targetY = 1
        break
    elif command == "2":
        targetY = 2
        break
    print("Invalid input!")
while 1:
    command = raw_input("Please enter a starting direction: ")
    if command == "east":
        bearing = 0
        break
    elif command == "north":
        bearing = 1
        break
    elif command == "west":
        bearing = 2
        break
    elif command == "south":
        bearing = 3
        break
    print("Valid directions are \"north\", \"south\", \"east\", and \"west\".")

calcMat(myX, myY, targetX, targetY, chicMat)

if instructions[0] == -2:
    ropi.right()
    time.sleep(0.5)
    ropi.setTurnBias(1)
elif instructions[0] == -1:
    ropi.right()
    time.sleep(0.2)
    ropi.setTurnBias(1)
elif instructions[0]  == 1:
    ropi.left()
    time.sleep(0.2)
    ropi.setTurnBias(0)
elif instructions[0] == 2:
    ropi.left()
    time.sleep(0.5)
    ropi.setTurnBias(0)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = np.array(frame.array)
        
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #using yellow
    lower = np.array([3,138,108])
    upper = np.array([31, 255, 255]) 
    yellow = cv2.inRange(hsv, lower, upper)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    mask = cv2.bitwise_and(yellow, blur)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2]
    cntSort = []

    ropi.forward()

    if len(cnts) > 0:
        for c in cnts:
            x,y,w,h = cv2.boundingRect(c)
            if cv2.contourArea(c) > 80 and y+h/2 > RESOLUTION_H*1/3:
                cntSort.append(c)

    if len(cntSort) > 0:
        cntMax = max(cnts, key=cv2.contourArea)
        xM,yM,wM,hM = cv2.boundingRect(cntMax)
        if xM+wM/2 < RESOLUTION_W/3:
            regionMax = 0
        elif xM+wM/2 < RESOLUTION_W*2/3:
            regionMax = 1
        else:
            regionMax = 2

        turnDelay = RESOLUTION_H-(yM+hM/2)
        turnDelay /= 11.7

        if interIter < len(instructions):
            if instructions[interIter] == -2:
                ropi.right()
                time.sleep(0.2)
                ropi.setTurnBias(1)
            elif instructions[interIter] == -1:
                turnRight(turnDelay)
            elif instructions[interIter] == 0:
                ropi.forward()
                time.sleep(1.0)
            elif instructions[interIter] == 1:
                turnLeft(turnDelay)
            elif instructions[interIter] == 2:
                ropi.left()
                time.sleep(0.2)
                ropi.setTurnBias(0)
            elif instructions[interIter] == 3:
                ropi.stop()
                time.sleep(2)
            updateBearing(instructions[interIter])
            interIter += 1

    if(ropi.requestObstacle() == 1):
        obstruction = 1
        updateBearing(2)
        calcMat(myX,myY,targetX,targetY,chicMat)
        obstruction = 0

    cv2.imshow("Result", mask)

    #if interIter < len(instructions):
    #    print(interIter, instructions[interIter])
    #print(myX, myY)

    rawCapture.truncate(0)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

ropi.stop()
cv2.destroyAllWindows()
