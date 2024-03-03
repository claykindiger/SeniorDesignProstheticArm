#!/usr/bin/env python3
#
# First, take a picture using the camera
# Then, once the picture is taken, classify the image
# Lastly, save the image with the bounding box and label.
#

from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, saveImage, Log

Log.SetLevel('Error')


##### LET'S TEST ImageNet too, since we are only classifying images...

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
#camera = videoSource("csi://0")      # '/dev/video0' for V4L2 ## OLD CAMERA
camera = videoSource("/dev/video0")
print('camera loaded')
#display = videoOutput("display://0") # 'my_video.mp4' for file


detections = []
t = 0

while detections == [] and t < 50:
    img = camera.Capture()
    print('check')
    if img is None: # capture timeout
        continue
	
    detections = net.Detect(img)

labels = []
for det in detections:
	labels.append(net.GetClassLabel(detections[0].ClassID))

print(f"The Model Predicted the Following Objects: {labels}")

saveImage("test_pic.jpg",img)

print("Saved resulting picture in test_pic.jpg")

camera.Close()
	

