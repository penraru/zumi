import os
import sys

import RoPi_SerialCom as ropi

sys.path.append('/usr/local/lib/python2.7/site-packages')

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

RESOLUTION_W = 160
RESOLUTION_H = 128import os
import sys

import RoPi_SerialCom as ropi

sys.path.append('/usr/local/lib/python2.7/site-packages')

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

RESOLUTION_W = 160
RESOLUTION_H = 128

elapsedTime = 0

loopCount = 0
camera = PiCamera()
camera.resolution = (RESOLUTION_W, RESOLUTION_H)
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera)
time.sleep(1) #overclocked pi

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = np.array(frame.array)
    #initTime = time.millis()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #greyscale?


    #using yellow
    #lower = np.array([0,0,140])
    #lower = np.array([2,255,171])
    lower = np.array([2,197,128])
    #lower = np.array([0,0,255])

    #upper = np.array([80,100,255])
    #upper = np.array([110,255,221])
    upper = np.array([30, 255, 255])
    #upper = np.array([127,10,255])
    blur = cv2.GaussianBlur(hsv, (5,5,),0) #blur for reducing noise
    mask = cv2.inRange(blur, lower, upper) #color filter to show desired color
    #blur = cv2.GaussianBlur(mask,(5,5),0) #blur for reducing noise

    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(contours) > 0:
        #yprint("contour(s) found!")
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)


        #finding center of the contour
        if int(M['m00']) != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = RESOLUTION_W
            cy = RESOLUTION_H


        cv2.line(mask,(cx,0),(cx,RESOLUTION_H),(255,0,0),1)
        cv2.line(mask,(0,cy),(RESOLUTION_W,cy),(255,0,0),1)

        cv2.drawContours(mask, contours, -1, (0,255,0),1)


        #navigate
        if loopCount > 10:
            ropi.setSpeed(10)
            if cx >= 90:
                print("RIGHT")
                ropi.right()
                currentState = "Right"

            elif cx < 90 and cx > 50:
                print("STRAIGHT")
                ropi.setSpeed(30)
                ropi.forward()
                currentState = "Straight"
                ropi.setSpeed(10)

            elif cx <= 50:
                print("LEFT")
                ropi.left()
                currentState = "Left"
            else:
                pass
                print("NO LINE")
                #ropi.stop()
            loopCount = 0
    loopCount+=1


    cv2.imshow("Result", frame)
    #cv2.imshow("Result", mask)
    rawCapture.truncate(0)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

ropi.stop()
cv2.destroyAllWindows()


elapsedTime = 0

loopCount = 0
camera = PiCamera()
camera.resolution = (RESOLUTION_W, RESOLUTION_H)
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera)
time.sleep(1) #overclocked pi

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = np.array(frame.array)
    #initTime = time.millis()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #greyscale?


    #using yellow
    #lower = np.array([0,0,140])
    #lower = np.array([2,255,171])
    lower = np.array([2,197,128])
    #lower = np.array([0,0,255])

    #upper = np.array([80,100,255])
    #upper = np.array([110,255,221])
    upper = np.array([30, 255, 255])
    #upper = np.array([127,10,255])
    blur = cv2.GaussianBlur(hsv, (5,5,),0) #blur for reducing noise
    mask = cv2.inRange(blur, lower, upper) #color filter to show desired color
    #blur = cv2.GaussianBlur(mask,(5,5),0) #blur for reducing noise

    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(contours) > 0:
        #yprint("contour(s) found!")
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)


        #finding center of the contour
        if int(M['m00']) != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = RESOLUTION_W
            cy = RESOLUTION_H


        cv2.line(mask,(cx,0),(cx,RESOLUTION_H),(255,0,0),1)
        cv2.line(mask,(0,cy),(RESOLUTION_W,cy),(255,0,0),1)

        cv2.drawContours(mask, contours, -1, (0,255,0),1)


        #navigate
        if loopCount > 10:
            ropi.setSpeed(10)
            if cx >= 90:
                print("RIGHT")
                ropi.right()
                currentState = "Right"

            elif cx < 90 and cx > 50:
                print("STRAIGHT")
                ropi.setSpeed(30)
                ropi.forward()
                currentState = "Straight"
                ropi.setSpeed(10)

            elif cx <= 50:
                print("LEFT")
                ropi.left()
                currentState = "Left"
            else:
                pass
                print("NO LINE")
                #ropi.stop()
            loopCount = 0
    loopCount+=1


    cv2.imshow("Result", frame)
    #cv2.imshow("Result", mask)
    rawCapture.truncate(0)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

ropi.stop()
cv2.destroyAllWindows()
