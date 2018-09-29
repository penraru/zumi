print("Use up, down, and right arrows to control Zumi. Down arrow to save training data to Cloud. Console loading...")

import sys
sys.path.insert(0,'/home/pi/zumi/lib')
import Engine as engine
import TrainingDataHelper as data_helper

import curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
# screen.nodelay(True)

from picamera import PiCamera
camera = PiCamera()
camera.resolution = (32, 32)
camera.start_preview()

command_number = 0
command = ""

def save_training_data():
    data_helper.upload_images_to_cloud()
    data_helper.clear_images_from_zumi()
    clean_up()
    
def clean_up():
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    camera.close()
    engine.stop()
    exit()

try:
    while True:
            
        char = screen.getch()
        if char == curses.KEY_RIGHT:
            command = 'right'
            engine.right_a_bit()
        elif char == curses.KEY_LEFT:
            command = 'left' 
            engine.left_a_bit()
        elif char == curses.KEY_UP:
            command = 'up' 
            engine.forward_a_bit()
        elif char == curses.KEY_DOWN:
            save_training_data()
                          
        screen.addstr(0, 0, command)
            
        command_number += 1
        fileName = "/home/pi/zumi/sample/deep-learning-demos/driving/images/" + str(command_number) + "." + command + ".jpg"
        camera.capture(fileName)
        command = ""
            
finally:
    clean_up()
    

