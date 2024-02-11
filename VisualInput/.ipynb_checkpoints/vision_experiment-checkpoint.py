import math
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, saveImage, Log

Log.SetLevel('Error')

net = detectNet("ssd-mobilenet-v2", threshold=0.5)

num_trials = 10

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
	
    min_label = None
    min_distance = 1000
    for det in detections:
        center = det.center
        distance = math.sqrt(center[0]**2 + center[1]**2)
        if distance < min_distance:
            min_distance = distance
            min_label = net.GetClassLabel(det.ClassID)

    camera.Close()
    
    return min_label

results = []

def run_trial(results,correct_label):
    starttime = time.time()
    label = classify_image(None)
    runtime = time.time() - starttime
    
    # results.append([label, correct_label, runtime])
    return [label, correct_label, runtime]
print('label     correct label      runtime')
for i in range(num_trials):
    results = run_trial(results,'bottle')
    print(f'{results[0]}     {results[1]}      {results[2]}')
    
