import detect
import actuator
import time
import sys
import os 
from writedata import *

turnedleft = False
turnedright = False


def move(dec,act,filepath):
	global turnedleft
	forward = 390 #380 not working, #390 can avoid at distance 2 meters
	stop = 373
	center = 363
	left = 455
	right = 272
	bias = 30
	if dec == None:
		writefile(filepath,center, forward)
		act.throttle(forward)
		act.steering(center)

	else:
		cam_height = 120
		cam_width = 160
		totalarea = cam_height*cam_width
		cam_center = cam_width//2
		if dec.Area < 0.1*totalarea: #too far ignore
			writefile(filepath,center, forward,dec.Area, dec.Center)
			act.throttle(forward)
			act.steering(center)
		elif dec.Area >= 0.8*totalarea: #too close to obstacle, stop!
			writefile(filepath,center, stop,dec.Area, dec.Center)
			act.throttle(stop)
			act.steering(center)
			sys.exit()
		else: #turn away from obstacle
			#print(dec.Center[0])
			d_from_center = abs(cam_center-dec.Center[0])
			
			if dec.Center[0] > cam_center and not turnedright: #object at right
				angle = center + ((-abs(center-left)/cam_center)*d_from_center+abs(center-left)+bias)
				writefile(filepath,angle, forward,dec.Area, dec.Center)
				act.steering(angle)
				act.throttle(forward)
				turnedleft = True

			elif dec.Center[0] <= cam_center and not turnedleft: #object at left
				angle = center - ((-abs(center-right)/cam_center)*d_from_center+abs(center-right)+bias)
				writefile(filepath,angle, forward,dec.Area, dec.Center)
				act.steering(angle)
				act.throttle(forward)
				turnedright = True
			
def checkangle(dec,filepath):
	global turnedleft
	forward = 390 #380 not working, #390 can avoid at distance 2 meters
	stop = 373
	center = 363
	left = 455
	right = 272
	bias = 30
	if dec == None:
		writefile(filepath,center, forward, "None", "None")
		print(center, forward, "None", "None")
	else:
		cam_height = 120
		cam_width = 160
		totalarea = cam_height*cam_width
		cam_center = cam_width//2
		if dec.Area < 0.1*totalarea: #too far ignore
			writefile(filepath,center, forward, dec.Area, dec.Center)
			print(center, forward, dec.Area, dec.Center)
		elif dec.Area >= 0.8*totalarea: #too close to obstacle, stop!
			writefile(filepath, center, stop,dec.Area, dec.Center)
			print(center, stop, dec.Area, dec.Center)
			sys.exit()
		else: #turn away from obstacle
			d_from_center = abs(cam_center-dec.Center[0])
			
			if dec.Center[0] > cam_center : #object at right   and not turnedright
				angle = center + ((-abs(center-left)/cam_center)*d_from_center+abs(center-left)+bias)
				writefile(filepath,angle, forward, dec.Area, dec.Center)
				print(angle, forward,dec.Area, dec.Center)
				#turnedleft = True

			elif dec.Center[0] <= cam_center : #object at left and not turnedleft
				angle = center - ((-abs(center-right)/cam_center)*d_from_center+abs(center-right)+bias)
				writefile(filepath,angle, forward, dec.Area, dec.Center)
				print(angle, forward, dec.Area, dec.Center)
				#turnedright = True
					
def main():
	dete = detect.detectnet()
	#act = actuator.actuator()
	filepath = findpath()

	while True:
		dec = dete.update()
		#move(dec,act,"lol")
		checkangle(dec,filepath)
			
			

if __name__ == "__main__":
	main()
	
	
