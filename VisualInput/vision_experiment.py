import math
from datetime import datetime 
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, saveImage, Log

Log.SetLevel('Error')

net = detectNet("ssd-mobilenet-v2", threshold=0.7)

num_trials = 5

def classify_image(net,trial_num):
    camera = videoSource("/dev/video0")
    
    center_frame = (camera.GetWidth()/2,camera.GetHeight()/2)
    print(center_frame)

    detections = []

    while detections == []:
        img = camera.Capture()

        if img is None: # capture timeout
            continue
		
        detections = net.Detect(img)
    
    saveImage(f"experiment/test_pic_{trial_num}.jpg",img)

    print("Saved resulting picture in test_pic.jpg")
	
    min_label = None
    min_distance = 1000000
    for det in detections:
        center = det.Center
        distance = math.sqrt((center[0]- center_frame[0])**2 + (center[1] - center_frame[1])**2)
        print(net.GetClassLabel(det.ClassID), distance,center)
        if distance < min_distance:
            min_distance = distance
            min_label = net.GetClassLabel(det.ClassID)

    camera.Close()
    
    return min_label

results = []

def run_trial(net, trial_num, results,correct_label):
    start = datetime.now()
    label = classify_image(net,trial_num)
    end = datetime.now()
    runtime = end - start
    
    # results.append([label, correct_label, runtime])
    return [label, correct_label, runtime]

print('trial num    label     correct label      runtime')

for i in range(num_trials):
    results = run_trial(net, i, results,'bottle')
    lab = results[0]
    corr_lab = results[1]
    time = results[2]
    print(i,lab,corr_lab,time)
    print()
    
