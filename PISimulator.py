# -*- coding:utf-8 -*-
from Simulator import Simulator
import random

class PISimulator(Simulator):
	def __init__(self, budget, unitPrice):
		Simulator.__init__(self, budget, unitPrice)
		self.Kp = - 100 / (budget * 0.25)
		self.Ki = -7
		self.OUTPUT_NAME = 'output2.csv'
		self.INTEGRAL_OFFSET_RATIO = 0.01
		self.errorIntegral = 0
		# INTEGRAL 에러 누적으로 windup 방지를 위해 만듦
		self.INTEGRAL_ERROR_LIMIT = 1

	def IsCap(self):
		cap = 100 + (self.Kp * (self.budget - self.spent)) + self.Ki * self.INTEGRAL_ERROR_LIMIT
		if cap < 0:
			cap = 0
		elif cap > 100:
			cap = 100
		else:
			cap = int(cap)
		# print cap
		if self.spent >= self.budget:
			return True
		if random.randrange(100) < cap:
			return True
		return False