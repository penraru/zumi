import sys
sys.path.insert(0,'/home/pi/zumi/lib')
import Engine as engine
import Infrared as infrared
import time
engine.start_line_follower()

while True:
    f=infrared.get_front_distance()
    print(f)
    if f<=300:
        engine.stop()
        time.sleep(.1)
        engine.turn_right()
        time.sleep(.6)
        engine.stop()
        time.sleep(.1)
        engine.start_line_follower()