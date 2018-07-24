import cv2

# Load a photo of Donald Trump
trump = cv2.imread('images/trump.jpg', cv2.IMREAD_COLOR)
# Resize Trump
trump = cv2.resize(trump,(800,450))

# Challenge: Use the openCV documentation to draw red eyes on Donald Trump
# https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html

cv2.circle(trump,(350,180), 12, (0,0,255), -1)
cv2.circle(trump,(430,180), 12, (0,0,255), -1)
cv2.imshow("tash", trump)
cv2.waitKey(0)

