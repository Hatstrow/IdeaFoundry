from machine import Pin
import time
class LightShow():
	def __init__(self, pin1,pin2,pin3):
		self.led1 = Pin(pin1, Pin.OUT)
		self.led1.value(1)
		self.led2 = Pin(pin2, Pin.OUT)
		self.led2.value(1)
		self.led3 = Pin(pin3, Pin.OUT)
		self.led3.value(1)
		print(self.led1.value())
		print(self.led2.value()) 
		print(self.led3.value())  

	def GoodGuys1(self):
		time.sleep(2)
		for i in range(3):
				self.led1.value(0)
				self.led2.value(1)
				self.led3.value(1)
				print('led1')
				time.sleep(.25)
				self.led1.value(1)
				self.led2.value(0)
				self.led3.value(1)
				print('led2')
				time.sleep(.25)
				self.led1.value(1)
				self.led2.value(1)
				self.led3.value(0)
				print('led3')
				time.sleep(1)
				self.led3.value(1)
				print('led33')
				time.sleep(.25)
				self.led2.value(1)
				print('led22')
				time.sleep(.25)
				self.led1.value(1)
				print('led11')
				time.sleep(.25)
				for i in range(5):
					time.sleep(.1)
					self.led3.value(0)
					time.sleep(.1)
					self.led3.value(1)

	def BadGuys1(self):
		time.sleep(2)
		self.led1.value(1)
		self.led2.value(1)
		self.led3.value(1)
		for i in range(5):
			time.sleep(.5)
			self.led1.value(0)
			time.sleep(.5)
			self.led1.value(1)
