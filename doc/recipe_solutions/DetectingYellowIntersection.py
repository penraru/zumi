from picamera.array import PiRGBArray
import picamera
import time
import IPython.display
import PIL.Image
import cv2
import numpy as np

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])

with picamera.PiCamera() as camera:
    camera.resolution = (220, 180)
    rawCapture = PiRGBArray(camera)
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array  #grab the raw NumPy array representing the image
        rawCapture.truncate(0) # clear the stream in preparation for the next frame
        
        # This image can now be used with openCV...
        image = cv2.flip(image, 0)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        cnt = 0
        for i in range(0,180,5):
            for j in range(0,220,5):
                if mask.item(i,j) == 255:
                    cnt = cnt + 1
                if cnt >= 100:
                    break
                    
        if cnt >= 100 :
            print("Intersection!")
        else :
            print("No intersection")
            
        IPython.display.display(PIL.Image.fromarray(mask))
                
        #IPython.display.display(PIL.Image.fromarray(image))
        IPython.display.clear_output(wait=True) 