#Code that allows Zumi to follow a white line on a black background

import sys
sys.path.insert(0,'/home/pi/zumi/lib')
sys.path.insert(0,'/home/pi/zumi/src')
import Infrared
import Linky_SerialCom as linky
import time

time.sleep(3) #Give the Pi time to boot up

currentTime = time.time()
engineStateOld = -1
turnPulse = 0

while 1:
	irBits = Infrared.get_bottom_colors() #Get the states of both bottom IR sensors
	if time.time() - currentTime > 0.5: #Slow down turns by forcing Zumi to stop at regular intervals
		turnPulse = 1 - turnPulse
		currentTime = time.time()
	if turnPulse == 0:
		if irBits == 0: #Both IR sensors detect white
			currentTime = time.time()
			engineState = 0
		elif irBits == 1: #Right IR sensor detects black
			engineState = 1
		elif irBits == 10: #Left IR sensor detects black
			engineState = 2
		elif irBits == 11: #Both IR sensors detect black
			engineState = 3
	else:
		engineState = 4
	if engineState != engineStateOld: #Only send a new commmand if it differs from the previous one
		if(engineState == 0):
			linky.setMotor(18,18) #Go forward
		elif(engineState == 1):
			linky.setMotor(-12,15) #Go left, and forward slightly
		elif(engineState == 2):
			linky.setMotor(15,-12) #Go right, and forward slightly
		elif(engineState == 3):
			linky.setMotor(15,-15) #Spin clockwise
		else:
			linky.stop()
		engineStateOld = engineState #Update engine state
