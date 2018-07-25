# CHALLENGE: Show frames from your web cam until a key is pressed

import cv2

while True:
    print "hi"
    cv2.namedWindow('Press Q to Quit', cv2.WINDOW_NORMAL)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print "done"


