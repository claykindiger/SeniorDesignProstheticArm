### Full Pipeline

from SeniorDesignProstheticArm.take_and_classify import classify_image

from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, saveImage, Log



## myoware running anomaly detection to detect flexion of muscle


## when flexion is detected, turn on the microphone


## run model on received sound


## if recognized grip input --> move hand to grip


## else (or if input is to turn camera on) --> run image detection


## convert return image label or audio to grip 

def label_to_grip(label):
    label_mapping = {}
    
    return label_mapping[label]

## run script to move hand to the position


        
