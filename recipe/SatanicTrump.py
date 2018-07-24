import cv2

# Load a photo of Donald Trump
trump = cv2.imread('images/trump.jpg', cv2.IMREAD_COLOR)
# Resize Trump
trump = cv2.resize(trump,(800,450))
# Show the image of Trump
cv2.imshow("tash", trump)
# Keep the image open until a key is pressed
cv2.waitKey(0)

# Challenge: Use the openCV documentation to draw red eyes on Donald Trump
# https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html




