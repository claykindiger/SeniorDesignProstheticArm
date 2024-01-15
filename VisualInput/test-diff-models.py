#!/usr/bin/env python3
#
# First, take a picture using the camera
# Then, once the picture is taken, classify the image
# Lastly, save the image with the bounding box and label.
#

import sys
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, saveImage, Log

Log.SetLevel('Error')

##### LET'S TEST ImageNet too, since we are only classifying images...
model = sys.argv[1]

net = detectNet(model, threshold=0.5)
#camera = videoSource("csi://0")      # '/dev/video0' for V4L2 ## OLD CAMERA
#display = videoOutput("display://0") # 'my_video.mp4' for file

num_classes = net.GetNumClasses()

print(num_classes)

#labels = {}
#for i in range(num_classes):
#	labels[i] = net.GetClassLabel(i)

#print(f"The Model Has the following labels: {labels}")

#with open(f'{model}_labels.txt', mode='w') as f:
#	f.write(str(labels))
#	f.close()

#print(f"Saved resulting labels in {model}_labels.txt")

	

