import Linky_SerialCom as linky
import time

THRESH = 940

time.sleep(2)
linky.setSpeed(20)
time.sleep(1)

print "Bottom Left:\tBottom Right:"

while 1:
	NULL,NULL,NULL,IR_BL,IR_BR,NULL,NULL = linky.readSensors()
	a = str(IR_BL) + "\t\t" + str(IR_BR)
	print a
	if IR_BL < THRESH and IR_BR < THRESH:
		linky.forward()
	elif IR_BL >= THRESH and IR_BR < THRESH:
		linky.left()
	elif IR_BL < THRESH and IR_BR >= THRESH:
		linky.right()
	else:
		linky.stop()
