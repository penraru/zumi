import numpy as np
import cv2

while 1:
        #Load image
	im = cv2.imread('images/Facevase.bmp')

	#Convert image to greyscale
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

	#Create threshold for contours by color
	ret,thresh = cv2.threshold(imgray,127,255,0)

	#Get contours
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	#Draw contours
	cv2.drawContours(im, contours, 0,(0,255,0), 3)

	#Show image
	cv2.imshow("Result",im)

	#Press Esc on the window to end the program
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()

# Challenge: One vase? Or two faces? Use contour detection to draw an outline around the vase is in this famous optical illusion
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html
