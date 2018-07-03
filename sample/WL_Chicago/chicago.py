import os
import sys

import RoPi_SerialCom as ropi

sys.path.append('/usr/local/lib/python2.7/site-packages')

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import random

#Initialize constants
RESOLUTION_W = 80
RESOLUTION_H = 64
PIZZA_X = 0
PIZZA_Y = 0

#Initialize variables
routeComplete = False
idleMode = False

chicMat = np.zeros([6,3])
myX = 0
myY = 0
targetX = 2
targetY = 2
bearing = 0
bearingTemp = 0
obstruction = 0
interIter = 0
instructions = []

def printInstructions():
    print(instructions)

def turnLeft():
    print("left")
    ropi.stop()
    ropi.stop()
    ropi.stop()
    ropi.forward()
    time.sleep(1.253)
    ropi.stop()
    ropi.left()
    time.sleep(0.25)
    ropi.stop()
    ropi.stumble()
    time.sleep(0.8)
    ropi.stop()

def turnRight():
    print("right")
    ropi.stop()
    ropi.stop()
    ropi.stop()
    ropi.forward()
    time.sleep(1.4)
    ropi.stop()
    ropi.right()
    time.sleep(0.29)
    ropi.stop()
    ropi.stumble()
    time.sleep(0.63)
    ropi.stop()
    print("finish right")

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
        print("obstruction")
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

camera = PiCamera()
camera.resolution = (RESOLUTION_W, RESOLUTION_H)
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera)
time.sleep(2)


calcMat(myX, myY, targetX, targetY, chicMat)
printInstructions()

if (instructions[0] == -2):
    print('right 180')
    ropi.right()
    time.sleep(0.56)
elif instructions[0] == -1:
    print('right 90')
    ropi.right()
    time.sleep(0.2)
elif instructions[0]  == 1:
    print('left 90')
    ropi.left()
    time.sleep(0.2)
elif instructions[0] == 2:
    print('left 180')
    ropi.left()
    time.sleep(0.56)

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

    #ropi.forward()

    if len(cnts) > 0:
        for c in cnts:
            x,y,w,h = cv2.boundingRect(c)
            if cv2.contourArea(c) > 14 and y+h/2 > RESOLUTION_H*1/3:
                cntSort.append(c)

    if len(cntSort) > 0:
        cntMax = max(cnts, key=cv2.contourArea)
        xM,y,wM,h = cv2.boundingRect(cntMax)
        if xM+wM/2 < RESOLUTION_W/3:
            regionMax = 0
        elif xM+wM/2 < RESOLUTION_W*2/3:
            regionMax = 1
        else:
            regionMax = 2

        if interIter < len(instructions):
            print("intersection")
            if instructions[interIter] == -2:
                ropi.right()
                time.sleep(0.56)
            elif instructions[interIter] == -1:
                turnRight()
            elif instructions[interIter] == 0:
                ropi.forward()
                time.sleep(1.0)
            elif instructions[interIter] == 1:
                turnLeft()
            elif instructions[interIter] == 2:
                ropi.left()
                time.sleep(0.56)
            updateBearing(instructions[interIter])
            interIter += 1
        else:
            routeComplete = True
            print("we made it!")
            ropi.forward()
            time.sleep(0.9)
            ropi.stop()
            ropi.stop()
            ropi.stop()
            ropi.victoryBeep() #end program
            break


    if(ropi.requestObstacle() == 1):
        obstruction = 1
        updateBearing(2)
        calcMat(myX,myY,targetX,targetY,chicMat)
        printInstructions()
        obstruction = 0

    if not routeComplete:
        ropi.forward()

    #cv2.imshow("Result", mask)

    #if interIter < len(instructions):
    #    print(interIter, instructions[interIter])
    #print(myX, myY)

    rawCapture.truncate(0)



ropi.stop()
cv2.destroyAllWindows()
