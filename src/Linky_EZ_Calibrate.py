import os
import FaBo9Axis_MPU9250
import time
import numpy as np

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
mx = []
my = []
mz = []

def getAvg(list = []):
	x = 0
	for i in range(0,len(list)):
		x = x + list[i]
	x = x/len(list)
	return x

#Display instructions
print("\nWelcome to the Linky EZ Calibration Software!\n")
print("To calibrate your Linky's magnetometers, press Enter, then slowly rotate your Linky for 30 seconds.\n")
print("For the best results, please do the following:")
print("-Keep your Linky as flat as possible")
print("-Power your Linky using a battery or long cable")
print("-Rotate your Linky in one direction at a constant speed\n")
raw_input("Press Enter to begin calibrating...")
print("Please rotate your Linky now.")

#Get magnetometer offsets
path = os.path.join(os.path.dirname(FaBo9Axis_MPU9250.__file__), 'config.txt')
if os.path.exists(path) == False:
	f = open(path,'w')
	f.write('MX_OFFSET = 0\n')
	f.write('MY_OFFSET = 0\n')
	f.write('MZ_OFFSET = 0')
	f.close()
f = open(path,'r')
for i in range(3):
	a = f.readline()
	b,c = a.split('=')
	if i == 0:
		mx_offset = float(c)
	elif i == 1:
		my_offset = float(c)
	else:
		mz_offset = float(c)
f.close()

#Begin calibration
currentTime = time.time()
f = open('EZcalib.txt','w')

while time.time() - currentTime < 30:
	mag = mpu9250.readMagnet()
	x = mag['x']
	y = mag['y']
	z = mag['z']
	mx.append(x)
	my.append(y)
	mz.append(z)
	a = str(mag['x']) + "," + str(mag['y']) + "," + str(mag['z'])
	f.write(a)
	f.write('\n')
	time.sleep(0.2)

f.close()
print("\nDone!")

while 1:
	print("\nYour offsets are:")
	a = "X Offset: "+str(getAvg(mx))
	print(a)
	a = "Y Offset: "+str(getAvg(my))
	print(a)
	a = "Z Offset: "+str(getAvg(mz))
	print(a)
	a = raw_input('\nType "testNew" or "testOld" to test your magnetometer with and without these offsets, respectively. Type "save" to keep these offests. This will modify your previously saved data. Type "exit" to keep your old offsets.\n')
	if a == "testNew" or a == "testOld":
		currentTime = time.time()
		if a == "testOld":
			b = 0
		else:
			b = 1
		print("\nX\tY\tZ\tBearing")
		while time.time() - currentTime < 15:
			mag = mpu9250.readMagnet()
			x = mag['x']
			y = mag['y']
			z = mag['z']
			x = x - getAvg(mx)*b
			y = y - getAvg(my)*b
			z = z - getAvg(mz)*b
			angle = np.arctan2(y,x)
			angle = np.degrees(angle)
			if angle < 0:
				angle = angle + 360
			a = str(x)+"\t"+str(y)+"\t"+str(z)+"\t"+str(angle)
			print a
			time.sleep(0.2)
	elif a == "save":
		f = open(path,'w')
		a = "MX_OFFSET = "+str(mx_offset+getAvg(mx))+"\n"
		f.write(a)
		a = "MY_OFFSET = "+str(my_offset+getAvg(my))+"\n"
		f.write(a)
		a = "MZ_OFFSET = "+str(mz_offset+getAvg(mz))
		f.write(a)
		f.close()
		break
	elif a == "exit":
		break
