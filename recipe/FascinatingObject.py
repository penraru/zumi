import cv2
webcam = cv2.VideoCapture(0)

# 1. Enter the HSV values for the fascinating object. You should have used the ColorCalibrator for this.
hue = 0
sat = 0
val = 0
hrange = 0
srange = 0
vrange = 0

def filterColor(frame):
   # Creates a boundary for the color that gets update by trackbars
    colorLower = (hue - hrange, sat - srange, val - vrange)
    colorUpper = (hue + hrange, sat + srange, val + vrange)

    # Creates a filtered frame that only captures colors within this range
    filteredFrame = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), colorLower, colorUpper)
    return filteredFrame

def get_best_contour():
    sortedCont = sorted(contoursArray, key=cv2.contourArea, reverse=True)[:3]
    return sortedCont[0]

while True:
    ret, frame = webcam.read()
    mask = filterColor(frame)
    mask = cv2.dilate(mask, None)
    mask = cv2.blur(mask, (21, 21))
    mask = cv2.dilate(mask, None)
    cv2.imshow('mask', mask)

    # Finds contours in the masked image
    contoursArray = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    # 2. Run this code to see if your object was found
    if len(contoursArray) == 0:
        print "Fascinating object not found :("
        break
    countour = get_best_contour()
    x, y, w, h = cv2.boundingRect(countour)

    print "Fascinating object found at x:" + str(x) + ", y:" + str(y)

    height, width, layers = frame.shape
    middleXpixel = width / 2

    # 3. CHALLENGE: Print whether the robot should move left or right to follow the fascinating object






    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()