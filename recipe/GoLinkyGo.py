import sys
import time
sys.path.insert(0,'/home/pi/Desktop/Linky/lib')
import Engine as engine

# To make Linky move, you should use her Engine.
# See her available functions at Linky/lib/Engine.py
# Try to make her go forward, stop and go backwards.

# WILLIAM: TO BE REMOVED ONCE TESTING IS COMPLETE 
# "FIXED" - WILLIAM
engine.go_forward()
time.sleep(1)
engine.stop()
time.sleep(1)
engine.go_backward()
time.sleep(1)
engine.stop()
