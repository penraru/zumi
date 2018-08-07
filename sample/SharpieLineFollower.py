import Linky_SerialCom as linky
import time

THRESH = 945
turnLeft = 0

time.sleep(2)
currentTime = time.time()

print "Bottom Left:\tBottom Right:"

while 1:
	NULL,NULL,NULL,IR_BL,IR_BR,NULL,NULL = linky.readSensors()
	a = str(IR_BL) + "\t\t" + str(IR_BR)
	print a
	if IR_BL < THRESH and IR_BR < THRESH:
		if time.time() - currentTime > 5:
			turnLeft = 1 - turnLeft
			currentTime = time.time() + 30
		if turnLeft == 0:
			linky.setMotor(12,-12)
		else:
			linky.setMotor(-12,12)
	elif IR_BL >= THRESH and IR_BR < THRESH:
		linky.setMotor(15,15)
		turnLeft = 1
		currentTime = time.time()
	elif IR_BL < THRESH and IR_BR >= THRESH:
		linky.setMotor(15,15)
		turnLeft = 0
		currentTime = time.time()
	else:
		linky.stop()
