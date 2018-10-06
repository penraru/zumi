# prep code for maker demo
print("Importing picamera...")
import picamera
import picamera.array

import sys
sys.path.insert(0, '/home/pi/zumi/lib')
print("Importing Engine...")
import Engine as engine

print("Importing Speaker...")
import Speaker as speaker

print("Importing numpy...")
import numpy as np

print("Importing PIL...")
from PIL import Image

print("Importing keras...")
from keras.models import load_model
from keras.preprocessing.image import img_to_array

import time

def coke():
    print("\n\n🍹 🍹 🍹 🍹 🍹 Coke! 🍹 🍹 🍹 🍹 🍹\n\n")
    engine.go_backward()
    time.sleep(2)
    engine.stop()
    speaker.play_sad_sound()

def apple():
    print("\n\n🍏 🍏 🍏 🍏 🍏 Apple! 🍏 🍏 🍏 🍏 🍏\n\n")
    engine.turn_right()
    time.sleep(3)
    engine.stop()
    speaker.play_happy_sound()
    
def nothing():
    print("\n\n\tNo object detected!\n\n")

functionsKey = {
        "1": nothing,
        "0": apple,
        "2": coke
        }

print("Loading model...")
#model = load_model('second_try.h5')
model = load_model('third_try.h5')

with picamera.PiCamera() as camera:
    try:
        while 1:
            with picamera.array.PiRGBArray(camera) as output:
                input("\n\nPress enter to start: ")
                camera.capture(output, 'rgb')
                x= Image.fromarray(output.array).resize((150,150))
                x = np.expand_dims(x, axis=0)
                pred = model.predict_classes(x)
                functionsKey[(str(int(pred)))]()
                
                #probs=model.predict_proba(x)
                #if probs[0][1]==1.0:
                #    nothing()
                #elif probs[0][0]==1.0:
                #    apple() 
                #elif probs[0][2]==1.0:
                #    coke()
                #else:
                #    nothing()
   

    except KeyboardInterrupt:
        print("\n\nExiting...\n\n")
