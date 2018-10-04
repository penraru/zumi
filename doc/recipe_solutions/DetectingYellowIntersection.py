from picamera.array import PiRGBArray
import picamera
import time
import IPython.display
import PIL.Image
import cv2
import numpy as np

lower_yellow = np.array([30, 100, 100])
upper_yellow = np.array([80, 255, 255])

with picamera.PiCamera() as camera:
    camera.resolution = (220, 180)
    rawCapture = PiRGBArray(camera)
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array  #grab the raw NumPy array representing the image
        rawCapture.truncate(0) # clear the stream in preparation for the next frame
        
        # This image can now be used with openCV...
        image = cv2.flip(image, 0)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
        IPython.display.display(PIL.Image.fromarray(mask))
        #IPython.display.display(PIL.Image.fromarray(image))
        IPython.display.clear_output(wait=True) 