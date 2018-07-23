import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/lib')
import Engine as engine
import Infrared as infrared
import time

# Use time.sleep(numberOfSeconds) to sleep Linky for 2 seconds before reading the IR sensors

# Use the Engine to drive forward

# In a loop, use the Infrared sensors to check if a wall is close
# Avoid the wall by turning in the opposite direction
