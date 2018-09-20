import sys
sys.path.insert(0,'/home/pi/zumi/lib')

import Engine as engine
import Infrared as infrared
import time
import IPython.display

# Use time.sleep(numberOfSeconds) to sleep Linky for 2 seconds before reading the IR sensors
time.sleep(2)
# Use the Engine to drive forward
engine.set_speed(15)
engine.go_forward()

# In a loop, use the Infrared sensors to check if a wall is close
# Avoid the wall by turning in the opposite direction
while 1:
    front_distance = infrared.get_front_distance()
    left_distance = infrared.get_left_distance()
    right_distance = infrared.get_right_distance()

    print (left_distance + " " + front_distance + " " + right_distance)
    if front_distance < 650 or left_distance < 600 or right_distance < 600 :
        print ("I might crash!")            
        engine.turn_right()
        time.sleep(1.1)
        engine.stop()
        time.sleep(0.3)
        engine.go_forward()
    
    IPython.display.clear_output(wait=True) 