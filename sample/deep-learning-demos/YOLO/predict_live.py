#! /usr/bin/env python

import argparse
import os
import cv2
import numpy as np
from tqdm import tqdm
from preprocessing import parse_annotation
from utils import draw_boxes
from frontend import YOLO
import json
import sys
import time
from flask import Flask

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"





with open('config.json') as config_buffer:
    config = json.load(config_buffer)

###############################
#   Make the model
###############################

yolo = YOLO(architecture        = config['model']['architecture'],
            input_size          = config['model']['input_size'],
            labels              = config['model']['labels'],
            max_box_per_image   = config['model']['max_box_per_image'],
            anchors             = config['model']['anchors'])

###############################
#   Load trained weights
###############################

print('yolo_powercube_model_final_backup.h5')
yolo.load_weights('yolo_powercube_model_final_backup.h5')
print("Loaded weights")
###############################
#   Predict bounding boxes
#######d########################

video_reader = cv2.VideoCapture(1)
frame_h = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_w = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Starting display')
master_time = time.time()
while True:
    ret, image = video_reader.read()
    if ret:
        print(int(((time.time() - master_time)*10))/10)
        master_time = time.time()
        boxes = yolo.predict(image)
        print(boxes)
        image = draw_boxes(image, boxes, config['model']['labels'])
        cv2.imshow('cube_detector', image)
        cv2.waitKey(1)
    else:
        print('BORK')

video_reader.release()


