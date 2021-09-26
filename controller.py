from writedata import *
import sys

# use to actuate the motors to move the car
def move(dec,act,filepath):
	forward = 390 #throttle forward
	stop = 373 #throttle stop
	center = 363 #angle center
	left = 455 #angle most left
	right = 272 #angle most right
	bias = 30 #bias if needed
	if dec == None:
		writefile(filepath,center, forward)
		act.throttle(forward)
		act.steering(center)

	else:
		cam_height = 120   #height of image
		cam_width = 160    #width of image
		totalarea = cam_height*cam_width #total area of image
		cam_center = cam_width//2  #camera center
		if dec.Area < 0.1*totalarea: #too far ignore
            writefile(filepath,center, forward, "None", "None")
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
			
			if dec.Center[0] > cam_center: #object at right
				angle = center + ((-abs(center-left)/cam_center)*d_from_center+abs(center-left)+bias)
				writefile(filepath,angle, forward,dec.Area, dec.Center)
				act.steering(angle)
				act.throttle(forward)
				turnedleft = True

			elif dec.Center[0] <= cam_center: #object at left
				angle = center - ((-abs(center-right)/cam_center)*d_from_center+abs(center-right)+bias)
				writefile(filepath,angle, forward,dec.Area, dec.Center)
				act.steering(angle)
				act.throttle(forward)
				turnedright = True

# use to check if the angle is determined correctly			
def checkangle(dec,filepath):
	global turnedleft
	forward = 390 #throttle forward
	stop = 373 #throttle stop
	center = 363 #angle center
	left = 455 #angle most left
	right = 272 #angle most right
	bias = 30 #bias if needed
	if dec == None:
		writefile(filepath,center, forward, "None", "None")
		print(center, forward, "None", "None")
	else:
		cam_height = 120   #height of image
		cam_width = 160    #width of image
		totalarea = cam_height*cam_width #total area of image
		cam_center = cam_width//2  #camera center
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


			elif dec.Center[0] <= cam_center : #object at left and not turnedleft
				angle = center - ((-abs(center-right)/cam_center)*d_from_center+abs(center-right)+bias)
				writefile(filepath,angle, forward, dec.Area, dec.Center)
				print(angle, forward, dec.Area, dec.Center)