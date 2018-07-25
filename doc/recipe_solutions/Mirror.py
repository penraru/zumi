# CHALLENGE: Show frames from your web cam until a key is pressed

import cv2
webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    cv2.imshow("Mirror, mirror on the wall...", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()


