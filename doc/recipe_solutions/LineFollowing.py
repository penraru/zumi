import sys
sys.path.insert(0,'/home/pi/zumi/lib')

import Engine as engine
import Infrared as infrared
import time

# Use time.sleep(numberOfSeconds) to sleep Zumi for 2 seconds
time.sleep(2)
# Use the Engine to start line following
engine.start_line_follower()
