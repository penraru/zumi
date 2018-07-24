import cv2

# Connect to your webcam
webcam = cv2.VideoCapture(0)

# Read a frame from your webcam
ret, frame = webcam.read()

# CHALLENGE: Display the frame read from your webcam
cv2.imshow('frame', frame)
cv2.waitKey(0)
