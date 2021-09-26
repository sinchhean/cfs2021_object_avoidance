import jetson.inference
import jetson.utils
import os

class detectnet(object):
	def __init__(self):
		self.network = "ssd-mobilenet-v2"
		self.threshold = 0.4
		self.overlay = "box,labels,conf"
		self.net = jetson.inference.detectNet(self.network, self.threshold)
		option1 = '--input-flip=rotate-180'
		option2 = "-input-width=160"
		option3 = "-input-height=120"
		self.input = jetson.utils.videoSource(argv=[option2,option3])
		self.output = jetson.utils.videoOutput()
		self.datanum = 0
		self.file = "./data/"
		i = 0
		while os.path.exists(self.file+str(i)):
			i += 1
		self.file = self.file + str(i) + "/"
		os.mkdir(self.file)
		os.mkdir(self.file+"image/")

	def update(self):
		# capture the next image
		img = self.input.Capture()

		# detect objects in the image (with overlay)
		detections = self.net.Detect(img, overlay=self.overlay)

		# print the detections
		#print("detected {:d} objects in image".format(len(detections)))

		#for detection in detections:
		#	print(detection)

		# render the image
		self.output.Render(img)
		jetson.utils.saveImageRGBA(self.file+"image/"+str(self.datanum)+".jpg",img)
		#print(img)
		self.datanum += 1

		# update the title bar
		#self.output.SetStatus("{:s} | Network {:.0f} FPS".format(self.network, self.net.GetNetworkFPS()))

		# print out performance info
		#self.net.PrintProfilerTimes()

		# exit on input/output EOS
		if not self.input.IsStreaming() or not self.output.IsStreaming():
			return 1

		
#   -- ClassID: 86
#   -- Confidence: 0.521484
#   -- Left:    593.125
#   -- Top:     7.20703
#   -- Right:   1020.62
#   -- Bottom:  719
#   -- Width:   427.5
#   -- Height:  711.793
#   -- Area:    304292
#   -- Center:  (806.875, 363.104)
		tmp = None
		m_area = 0
		for dec in detections: #class 86 vase, class 44 bottle, class 47 cup
			if (dec.ClassID == 44 or dec.ClassID == 86 or dec.ClassID == 47):
				if dec.Area > m_area:
					m_area = dec.Area
					tmp = dec

		return tmp
			


if __name__ == "__main__":
	
	pass
	de = detectnet()
	while True:
		dec = de.update()
		if dec != None:
			print(dec)
