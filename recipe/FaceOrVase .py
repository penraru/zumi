import numpy as np
import cv2

while 1:
        #Load image
	im = cv2.imread('images/Facevase.bmp')

	#Show image
	cv2.imshow("Result",im)

	#Press Esc on the window to end the program
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()

# Challenge: One vase? Or two faces? Use contour detection to show where the vase is in this famous optical illusion
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html
