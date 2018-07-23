import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/lib')
import Infrared as infrared
import time

# Use time.sleep(numberOfSeconds) to sleep Linky for 2 seconds before reading the IR sensors
time.sleep(2)

# Use a loop to continually read the front distance and test it with your finger
while 1:
    print "front: " + str(infrared.get_front_distance()) + " left: " + str(infrared.get_left_distance()) + " right: " + str(infrared.get_right_distance()) + " "
