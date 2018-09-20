import sys
sys.path.insert(0,'/home/pi/Zumi/lib')

import Engine as engine
import Infrared as infrared
import time

# while(True):
# #if distance is more than 10 cm. go back. Ig there is an obstacle stop
# #        if (ultrasonicSensorBack.get_distance() > 10):
# #                vikingbotMotors.goBack()

#     cmd = input("Enter the command ")
#     print(cmd)
#     if cmd == 'w':
#         engine.go_forward()
#     elif cmd == 'a':
#         engine.turn_left()
#     elif cmd == 's':
#         engine.turn_right()
#     else: 
#         engine.stop()

import curses

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

engine.set_speed(15)

try:
    while True:
        char = screen.getch()
        if char == ord('q'): 
            break
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(0, 0, 'right')
            engine.turn_right()
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ') 
            engine.turn_left()
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up   ') 
            engine.go_forward()
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
            engine.stop()
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()