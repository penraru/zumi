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

RESOLUTION_W=80
RESOLUTION_H=64
# sets resolution

camera=PiCamera()
camera.resolution=(RESOLUTION_W,RESOLUTION_H)
camera.hflip=True
camera.vflip=True
#flips the camera vertically and horizontally.
rawCapture = PiRGBArray(camera)
time.sleep(2)
print('done setup')
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = np.array(frame.array)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #detecting frames
    lower=np.array([100,150,0])
    upper=np.array([140,255,255])
    print('start loop') #sets upper and lower range
    mask = cv2.inRange(hsv, lower, upper)  # color filter to show desired color
    blur = cv2.GaussianBlur(mask, (5, 5), 0)  #blurs
    contours = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(contours) > 0:
        print("contour(s) found!") #controur=series of lists.
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = RESOLUTION_W
            cy = RESOLUTION_H


        cv2.line(mask,(cx,0),(cx,RESOLUTION_H),(255,0,0),1)
        cv2.line(mask,(0,cy),(RESOLUTION_W,cy),(255,0,0),1)

        cv2.drawContours(mask, contours, -1, (0,255,0),1)
        ropi.setSpeed(60)
        if cx>=60:
            ropi.right()
            print("IT is heading right")
            time.sleep(0.3)
            ropi.forward()
            time.sleep(0.2)
            ropi.stop()
        elif cx<60 and cx>20:
            ropi.forward()
            time.sleep(0.9)
            ropi.stop()
            print("it is heading straight")
        elif cx<20:
            ropi.left()
            print("it is turning left!!!!")
            time.sleep(0.3)
            ropi.forward()
            time.sleep(0.2)
            ropi.stop()
        else:
            ropi.stop()
            print("Emergency situation!")

    rawCapture.truncate(0)
