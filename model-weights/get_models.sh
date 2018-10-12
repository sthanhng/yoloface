#!/usr/bin/env bash

wget https://pjreddie.com/media/files/yolov3.weights
wget https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg?raw=true -O ./yolov3.cfg
wget https://github.com/pjreddie/darknet/blob/master/data/coco.names?raw=true -O ./coco.names

# for face detection using the YOLOv3 algorithm, you navigate to the below link:
# https://drive.google.com/file/d/1xYasjU52whXMLT5MtF7RCPQkV66993oR/view?usp=sharing
# to download the weights of the trained model
# put then it into the model-weights/ folder