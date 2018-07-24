import cv2

cutest = cv2.imread('images/axolotl.jpg', cv2.IMREAD_COLOR)
flipped = cv2.flip(cutest, -1)
cv2.imshow('image', flipped)
cv2.waitKey(0)
