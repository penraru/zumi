import FaBo9Axis_MPU9250
import time
import numpy as np
import Linky_SerialCom as ropi

MAG_X_OFFSET = 15.197
MAG_Y_OFFSET = 34.430

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
currentTime = time.time()

def getAngle():
	mag = mpu9250.readMagnet()
	x = mag['x']
	y = mag['y']
	x = x - MAG_X_OFFSET
	y = y - MAG_Y_OFFSET
	angle = np.arctan2(y,x)
	angle = np.degrees(angle)
	if angle < 0:
		angle = angle + 360
	return angle

time.sleep(1)
initAngle = getAngle()

time.sleep(2)
ropi.speed(30)

while time.time() - currentTime < 10:
	currentAngle = getAngle()
	if initAngle - currentAngle > 180:
		currentAngle = currentAngle + 360
	if currentAngle - initAngle >= 80:
		break
	ropi.left()
	print(currentAngle)
	time.sleep(0.15)

ropi.stop()
