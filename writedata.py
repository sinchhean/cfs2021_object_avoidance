import os

def findpath():
	filepath = "./data/"
	i = 0
	while os.path.exists(filepath+str(i)):
		i += 1
	filepath = filepath + str(i-1) + "/"
	return filepath

def writefile(filepath,steering, throttle, area, center):
	tmp_file = open(filepath+"log.txt","a")
	tmp_file.writelines(str(steering) + ", " + str(throttle)+ ", " + str(area)+ ", " + str(center) + "\n")
	tmp_file.close()
