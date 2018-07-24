import cv2

# Connect to your webcam
webcam = cv2.VideoCapture(0)

# Read a frame from your webcam
ret, frame = webcam.read()

# CHALLENGE: Display the frame that's been read from your webcam
