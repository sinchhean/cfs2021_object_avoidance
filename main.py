import detect
import actuator
import time
import sys
import os 
from writedata import *
from controller import *

			
def main():
	dete = detect.detectnet()
	#act = actuator.actuator()
	filepath = findpath()

	while True:
		dec = dete.update()
		#move(dec,act,filepath) #for moving the car
		checkangle(dec,filepath) #for checking angle
			
			

if __name__ == "__main__":
	main()
	
	
