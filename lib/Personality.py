import time
import sys
sys.path.insert(0,'/home/pi/zumi/lib')
import Engine as engine
import Infrared as infrared
import Speaker as speaker

def happy_zumi():
#     speaker.play_happy_sound()
    time.sleep(.5)
    engine.set_speed(30)
    engine.turn_left()
    engine.turn_right()
    engine.turn_left()
    engine.turn_right()
    engine.turn_left()
    engine.turn_right()
    engine.stop()
#     speaker.play_happy_sound()
    
import Linky_SerialCom as ropi 

def sad_zumi():
    baseline_speed = 15
    speed_difference = 10
    curve_duration = .5

    ropi.setMotor(-baseline_speed+speed_difference,-baseline_speed)
    time.sleep(curve_duration)
    ropi.setMotor(-baseline_speed,-baseline_speed+speed_difference)
    time.sleep(curve_duration)

    ropi.setMotor(-baseline_speed+speed_difference,-baseline_speed)
    time.sleep(curve_duration)
    ropi.setMotor(-baseline_speed,-baseline_speed+speed_difference)
    time.sleep(curve_duration)

    engine.stop()
    speaker.play_sad_sound()
    
def excited_zumi():
    engine.set_speed(45)
    engine.turn_right()
    time.sleep(1)
    engine.stop()