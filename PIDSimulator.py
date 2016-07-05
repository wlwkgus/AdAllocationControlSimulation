# -*- coding:utf-8 -*-
from __future__ import division
from Simulator import Simulator
import random

class PIDSimulator(Simulator):
	def __init__(self, budget, unitPrice):
		Simulator.__init__(self, budget, unitPrice)
		self.Kp = - 100 / (budget * 0.25)
		self.Ki = -5
		self.Kd = 10 / (unitPrice * 50)
		if self.budget < unitPrice * 10000:
			self.Kp = -100 / (budget * 0.999)
			self.Kd = 30 / (unitPrice * 20)
		self.OUTPUT_NAME = 'output3.csv'
		self.INTEGRAL_OFFSET_RATIO = 0.01
		self.errorIntegral = 0
		# INTEGRAL 에러 누적으로 windup 방지를 위해 만듦
		self.INTEGRAL_ERROR_LIMIT = 1
	def IsCap(self):
		dError = self.Kd * (self.spent - self.past_spent)
		# if (self.spent - self.past_spent) / self.unitPrice < 30:
		# 	dError = -0
		# print "now : " + str(self.spent) + " now-1 : " + str(self.past_spent) + " / " + str(dError)
		if self.now == 0:
			dError = 0
		# print dError
		if dError >= 30:
			dError = 30
		cap = 100 + (self.Kp * (self.budget - self.spent)) + self.Ki * self.INTEGRAL_ERROR_LIMIT + dError
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