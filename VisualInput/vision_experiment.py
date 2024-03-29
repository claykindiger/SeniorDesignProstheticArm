import math
import pandas as pd
from datetime import datetime 
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, saveImage, Log

Log.SetLevel('Error')

net = detectNet("ssd-mobilenet-v2", threshold=0.7)

num_trials = 50
dist_from_obj = '3ft'

def classify_image(net,trial_num):
    camera = videoSource("/dev/video0")
    
    center_frame = (camera.GetWidth()/2,camera.GetHeight()/2)
    #print(center_frame)

    detections = []

    attempts = 0
    while detections == []:
    	attempts += 1
    	img = camera.Capture()
    	if img is None: # capture timeout
    		#print(attempts)
    		if attempts == 10:
    			return None,attempts
    		continue
    	if attempts == 10:
    		return None,attempts
    	detections = net.Detect(img)
    	
    #saveImage(f"experiment/test_pic_{trial_num}.jpg",img)

    #print("Saved resulting picture in test_pic.jpg")
	
    min_label = None
    min_distance = 1000000
    for det in detections:
        center = det.Center
        distance = math.sqrt((center[0]- center_frame[0])**2 + (center[1] - center_frame[1])**2)
        #print(net.GetClassLabel(det.ClassID), distance,center)
        if distance < min_distance:
            min_distance = distance
            min_label = net.GetClassLabel(det.ClassID)

    camera.Close()
    
    return min_label,attempts

results = []

def run_trial(net, trial_num, results, correct_label):
    start = datetime.now()
    label,attempts = classify_image(net,trial_num)
    end = datetime.now()
    runtime = end - start
    
    # results.append([label, correct_label, runtime])
    return [label, correct_label, runtime, attempts]

print('trial num    label     correct label      runtime')

data = []
for i in range(num_trials):
	print(i)
	results = run_trial(net, i, results,'cup')
	res = {}
	res['predicted_label'] = results[0]
	res['correct_label'] = results[1]
	res['runtime'] = results[2]
	res['attempts'] = results[3]
	res['distance'] = dist_from_obj
	data.append(res)

data = pd.DataFrame(data)
data.to_csv(f"./experiment_results_{dist_from_obj}.csv")
    
   
