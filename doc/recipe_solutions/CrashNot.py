import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/lib')
import Engine as engine
import Infrared as infrared
import time

# Use time.sleep(numberOfSeconds) to sleep Linky for 2 seconds before reading the IR sensors
time.sleep(2)

# Use the Engine to drive forward
engine.go_forward()

# In a loop, use the Infrared sensors to check if a wall is close
# Avoid the wall by turning in the opposite direction

while (1):
    leftDistance = infrared.get_left_distance()
    rightDistance = infrared.get_right_distance()
    if leftDistance < 200:
        engine.turn_right()
    elif rightDistance < 200:
        engine.turn_left()