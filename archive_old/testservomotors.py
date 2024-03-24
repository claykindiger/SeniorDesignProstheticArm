import time
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)

## CLOSED ANGLE == 0
# Thumb touching index finger
## OPEN ANGLE == 180
## NEUTRAL (assume starts here) ANGLE == 60
#0 - INDEX
#1 - MIDDLE
#2 - RING
#3 - PINKY
#4 - THUMB

def point():
	desired_angles = {0:180,1:0,2:0,3:0,4:0}
	old_angle = [60,60,60,60,60]
	for i in range(0,100):
		for j in range(5):
			if j != 0:
				continue
			curr_angle = kit.servo[j].angle
			change = desired_angles[j]/100.0 -.6
			print(change)
			kit.servo[j].angle=curr_angle+change
			if j == 0:
				print(kit.servo[j].angle,desired_angles[j] - 60)
		time.sleep(.05)

def return_to_base():
	kit.servo[0].angle=60
	kit.servo[1].angle=60
	kit.servo[2].angle=60
	kit.servo[3].angle=60
	kit.servo[4].angle=60

def run(grip):
	if grip == 'point':
		point()
	else:
		return
	time.sleep(5)
	return_to_base()
	
kit.servo[0].angle=60
kit.servo[1].angle=60
kit.servo[2].angle=60
kit.servo[3].angle=60
kit.servo[4].angle=60

run('point')



