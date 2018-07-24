# Challenge: display only the red in the Where's Waldo image

import cv2
import numpy as np

frame = cv2.imread('images/waldo2.jpg', cv2.IMREAD_COLOR)

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of red color in HSV
lower_red = np.array([0,100,100])
upper_red = np.array([20,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_red, upper_red)

# Bitwise-AND mask and original image
reds = cv2.bitwise_and(frame, frame, mask=mask)

cv2.imshow('frame', frame)
cv2.imshow('res', reds)
cv2.waitKey(0)
