import cv2
import time

bird = cv2.imread('images/bigbird.jpg', cv2.IMREAD_COLOR)
current_time = time.time()
bird = cv2.flip(bird, -1)
print "color time:"
print time.time() - current_time

greyscale_bird = cv2.cvtColor(bird, cv2.COLOR_BGR2GRAY)

current_time = time.time()
greyscale_bird = cv2.flip(greyscale_bird, -1)
print "gray time:"
print time.time() - current_time

cv2.imshow('frame', bird)
cv2.waitKey(0)
