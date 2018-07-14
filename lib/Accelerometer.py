import time
import sys
sys.path.insert(0,'/home/pi/Desktop/Linky/src')
import Linky_SerialCom as ropi
import Accelerometer_Communication as accel

def turn_left():
    time.sleep(2)
    ropi.setMotor(-20, 20)
    stop_when_turned(90)

def turn_right():
    time.sleep(2)
    ropi.setMotor(20, -20)
    stop_when_turned(90)


def stop_when_turned(degrees):
    millis = int(round(time.time() * 1000))
    angle = 0.0
    while abs(angle) < degrees:
        if int(round(time.time() * 1000)) - millis >= accel.GYRO_SAMPLERATE:
            angle = accel.get_change_in_angle(angle)
            millis = int(round(time.time() * 1000))  # reset the time
    ropi.stop()
    print "stopped after " + str(angle) + " degrees"