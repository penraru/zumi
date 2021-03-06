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

RESOLUTION_W = 160
RESOLUTION_H = 128

camera = PiCamera()
camera.resolution = (RESOLUTION_W, RESOLUTION_H)
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera)
time.sleep(1) #overclocked pi

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = np.array(frame.array)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #using yellow
    #lower = np.array([0,0,140])
    #lower = np.array([2,255,171])
    lower = np.array([2,197,128])
    #upper = np.array([80,100,255])
    #upper = np.array([110,255,221])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper) #color filter to show desired color
    blur = cv2.GaussianBlur(mask,(5,5),0) #blur for reducing noise

    contours = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(contours) > 0:
        print("contour(s) found!")
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)


        #finding center of the contour
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
        else:
            cx = RESOLUTION_W
            cy = RESOLUTION_H


        cv2.line(mask,(cx,0),(cx,RESOLUTION_H),(255,0,0),1)
        cv2.line(mask,(0,cy),(RESOLUTION_W,cy),(255,0,0),1)

        cv2.drawContours(mask, contours, -1, (0,255,0),1)


      # navigate
      # ropi.setSpeed(30)
      # ropi.forward()
      # counter = 0

      if cx >= 100:
          if counter > 10:
              print("RIGHT")
              ropi.setSpeed(10)
              ropi.right()
              counter = 0
          # time.sleep(0.3)
          # ropi.stop()
          # ropi.forward()
          # time.sleep(0.2)
          counter += 1

      elif cx < 100 and cx > 70:
          if counter > 10:
              ropi.setSpeed(30)
              print("STRAIGHT")
              ropi.forward()
              # time.sleep(0.3)
              # ropi.stop()
              counter = 0
          counter += 1
      elif cx <= 70:
          if counter > 10:
              print("LEFT")
              ropi.setSpeed(10)
              ropi.left()
              counter = 0
          # time.sleep(0.3)
          # ropi.stop()
          # ropi.forward()
          counter += 1

    else:
    ropi.stop()

    # cv2.imshow("Result", mask)


rawCapture.truncate(0)

# key = cv2.waitKey(1) & 0xFF
