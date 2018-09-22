import sys
sys.path.insert(0,'/home/pi/zumi/lib')
import Engine as engine
engine.set_speed(15)

import curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(True)

from picamera import PiCamera
camera = PiCamera()
camera.resolution = (32, 32)
camera.start_preview()

frame_index = 0
command = ""

try:
    while True:
            
        char = screen.getch()
        if char == ord('q'): 
            camera.close()
            break
        elif char == curses.KEY_RIGHT:
            command = 'right'
            engine.right_a_bit()
        elif char == curses.KEY_LEFT:
            command = 'left' 
            engine.left_a_bit()
        elif char == curses.KEY_UP:
            command = 'up' 
            engine.forward_a_bit()
        elif char == curses.KEY_DOWN:
            command = "down"
            engine.back_a_bit()
        else:
            engine.stop()
            
        screen.addstr(0, 0, command)
            
        frame_index += 1
        fileName = "/home/pi/zumi/sample/deep-learning-demos/driving/images/" + str(frame_index) + "." + command + ".jpg"
        camera.capture(fileName)
        command = ""
            
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    camera.close()
