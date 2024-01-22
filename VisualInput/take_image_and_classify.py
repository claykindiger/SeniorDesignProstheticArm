#!/usr/bin/env python3
#
# First, take a picture using the camera
# Then, once the picture is taken, classify the image
# Lastly, save the image with the bounding box and label.
#


## TODO: test camera turn on time (should we keep it on all the time)
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, saveImage, Log

Log.SetLevel('Error')


##### LET'S TEST ImageNet too, since we are only classifying images...

def classify_image():
    net = detectNet("ssd-mobilenet-v2", threshold=0.5)
    #camera = videoSource("csi://0")     ## OLD CAMERA
    camera = videoSource("/dev/video1")


    detections = []

    while detections == []:
        img = camera.Capture()

        if img is None: # capture timeout
            continue

        detections = net.Detect(img)

    labels = []
    for det in detections:
        labels.append(net.GetClassLabel(detections[0].ClassID))

    camera.Close()
    
    return labels[0]

    
    
	

