import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

## CLOSED_ANGLE = 0
# 0 - INDEX
# 1 - MIDDLE
# 2 - RING
# 3 - PINKY
# 4 - THUMB

def point():
	desired_angle = {0:180,1:0,2:0,3:0,4:0}
	original_angle = [60,60,60,60,60]
	for i in range(0,50):
		for j in range(5):
			curr_angle = kit.servo[j].angle
			change = (desired_angle[j]-original_angle[j])/50
			if ( curr_angle + change < 0 ) | ( curr_angle + change > 180 ) :
				continue
			kit.servo[j].angle = curr_angle + change
		time.sleep(.01)

def ily():
	desired_angle = {0:180,1:0,2:0,3:180,4:180}
	original_angle = [60,60,60,60,60]
	for i in range(0,50):
		for j in range(5):
			curr_angle = kit.servo[j].angle
			change = (desired_angle[j]-original_angle[j])/50
			if ( curr_angle + change < 0 ) | ( curr_angle + change > 180 ) :
				continue
			kit.servo[j].angle = curr_angle + change
		#time.sleep(.001)
		
		
def return_to_base():
	kit.servo[0].angle = 60
	kit.servo[1].angle = 60
	kit.servo[2].angle = 60
	kit.servo[3].angle = 60
	kit.servo[4].angle = 60
	
def run(grip):
	return_to_base()
	if grip == 'point':
		point()
	elif grip == 'ily':
		ily()
	else:
		return
	## need to reevaluate stopping mechanism
	time.sleep(5)
	return_to_base()
	for i in range(5):
		print(i, kit.servo[i].angle)
## About 6.4 seconds to run, but 5 of them are built in...
start = time.time()	
run('ily')
print(time.time() - start)

	
			
