#For the cap parameters, replace the values with four different variables
#Contstruct a control panel to mess with the values to adjust the roi
#----------------
import sys
import cv2
import numpy as np
import math
def dist(x1,x2,y1,y2):
    return pow((x2-x1),2)+pow((y2-y1),2)
def tanDegree(x):
    deg=math.degrees(x)
    tan=math.tan(deg)
    return tan

img = cv2.VideoCapture(0)
img.set(3, 640) #width
img.set(4, 360) #height
while (1):
    ret, frame = img.read()
    cap = frame[350:400, 0:3000]#frame[height, width]
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    #cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    edges = cv2.Canny(gray, 100, 200, apertureSize=3)
    cv2.imshow("Can", edges)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, maxLineGap=90)
    max = 0,0,0,0
    max_dist = 0
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            line_dist =dist(x1,x2,y1,y2)
            if line_dist > max_dist:
                max = line[0]
                max_dist = line_dist
            # if  val > 10000:
            #     x1, y1, x2, y2 = val
            #     cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    x1, y1, x2, y2 = max
    bottom = x2-x1
    if bottom != 0:
        slope = (y2-y1)/(x2-x1)
        if max_dist>405585*0.7:
            if slope< tanDegree(0.174533) and slope> tanDegree(-0.174533):
                cv2.line(cap, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow("cap", cap)
    #cv2.imshow("frame", frame)
    # print("Width :" + str(cap.get(3)))
    # print("Height :" + str(cap.get(4)))
    print(max_dist)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
img.release()
cv2.destroyAllWindows()

