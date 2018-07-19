import sys
import time
sys.path.insert(0,'/home/pi/Desktop/Linky/lib')
import Engine as engine

engine.go_forward()
time.sleep(3)
engine.stop()
