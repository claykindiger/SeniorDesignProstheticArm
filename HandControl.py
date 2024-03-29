### Full Pipeline


from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, saveImage, Log
import speech_recognition
import runpca
import time

print('Modules Loaded...')

Log.SetLevel('Error')

net = detectNet("ssd-mobilenet-v2", threshold=0.5)

print('Model Loaded...')

################################# Classification functions

def catchAudio(commands):
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone(device_index=11) as mic:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic, 2, 2)
                text = recognizer.recognize_google(audio,show_all=True)
                possible_comms = []
                for i in text['alternative']:
                	possible_comms.append(i['transcript'].lower())
           
                print(possible_comms)
                break
        except Exception as e:
        	print(e)
        	print("Please say command again")
            #recognizer = speech_recognition.Recognizer()


    for ind, command in enumerate(commands):
        if command in possible_comms:
            print(command.capitalize())
            text = command
            break
        elif ind == (len(commands) - 1):
            print("Command not found. Word given: " + text)

    return text
    
def classify_image(net):
    camera = videoSource("/dev/video1")

    detections = []

    while detections == []:
        img = camera.Capture()

        if img is None: # capture timeout
            continue
		
        detections = net.Detect(img)
    
    saveImage("test_pic.jpg",img)

    print("Saved resulting picture in test_pic.jpg")
		
    labels = []
    for det in detections:
        labels.append(net.GetClassLabel(detections[0].ClassID))

    camera.Close()
    
    return labels[0]
    
############################################## Helper Functions

def label_to_grip(label):
    label_mapping = {'SmallWrap':[27,28,31,33,48,49,50,75,87,89,90], 'LargeWrap': [26,29,34,39,40,44,45,46,47,51,73,77,84,86,88], 'PowerSphere':[37,55,71]}
    
    for grip,labels in label_mapping.items():
	    if label in labels:
	    	command = grip
				
    return grip
    
################################################# Main Algorithm

test = True

commands = ['precision', 'point', 'enemy', 'middle', 'vision','small wrap']

## myoware running anomaly detection to detect flexion of muscle


## when flexion is detected, turn on the microphone
if test:
	command = catchAudio(commands)

## if recognized grip input --> move hand to grip
if command in commands:

	## else (or if input is to turn camera on) --> run image detection
	print(command)
	if command != 'vision':
		grip = command
		print('move hand here')
		
	else:
		print('using image classification')
		label = classify_image(net)
		
		# convert returned image label to grip
		command = label_to_grip(label)
		
## run script to move hand to the position

if command == 'point':
	runpca.point()
elif command == 'SmallWrap' or command == 'small wrap':
	runpca.small_grasp_out()
else:
	print('Grip not found...')

## For now, depends on how we want to indicate the release of an object
time.sleep(5)
runpca.neutral()



        
