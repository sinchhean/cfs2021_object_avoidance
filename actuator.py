from lib.PCA9685 import PCA9685
import smbus

class actuator():
	def __init__(self):
		busnum = 1
		bus = smbus.SMBus(busnum)
		i2c_address = 0x40
		hz = 60
		initial_value = 373
		self.pca9685 = PCA9685(bus, value=initial_value, address=i2c_address)
		self.pca9685.set_hz(hz)
		self.max_pulse = 483  #forward
		self.min_pulse = 263  #backward
		self.zero_pulse = 373 #stop
		self.left_pulse = 455 #turn left
		self.right_pulse = 272 #turn right
		self.center_pulse = 363 #center

	def safty_check(self, channel, pulse):
		if channel == 1:
			if pulse > self.max_pulse:
				pulse = self.max_pulse
			elif pulse < self.min_pulse:
				pulse = self.min_pulse
		if channel == 1:
			if pulse > self.left_pulse:
				pulse = self.left_pulse
			elif pulse < self.right_pulse:
				pulse = self.right_pulse
		return pulse

	def throttle(self,pulse):
		channel = 1
		#self.safty_check(channel, pulse)
		self.pca9685.set_channel_value(channel,pulse)

	def steering(self,pulse):
		channel = 0
		#self.safty_check(channel, pulse)
		self.pca9685.set_channel_value(channel,pulse)

if __name__ == "__main__":
	pass		
