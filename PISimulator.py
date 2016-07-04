# -*- coding:utf-8 -*-
from Simulator import Simulator
import random

class PISimulator(Simulator):
	Kp = -300
	Ki = -5
	OUTPUT_NAME = 'output2.csv'
	INTEGRAL_OFFSET_RATIO = 0.01
	errorIntegral = 0
	# INTEGRAL 에러 누적으로 windup 방지를 위해 만듦
	INTEGRAL_ERROR_LIMIT = 1
	def IsCap(self):
		self.IntegralError()
		cap = 100 + (self.Kp * (self.budget - self.spent) / self.budget) + self.Ki * self.errorIntegral / self.budget
		if cap < 0:
			cap = 0
		elif cap > 100:
			cap = 0
		else:
			cap = int(cap)
		# print cap
		if self.spent >= self.budget:
			return True
		if random.randrange(100) < cap:
			return True
		return False

	def IntegralError(self):
		if self.errorIntegral >= self.INTEGRAL_ERROR_LIMIT * self.budget:
			if (self.budget - self.timeSpent[self.now]) > 0:
				return
		if self.errorIntegral <= -self.INTEGRAL_ERROR_LIMIT * self.budget:
			if (self.budget - self.timeSpent[self.now]) < 0:
				return

		self.errorIntegral += self.budget - self.timeSpent[self.now]


		# for i in xrange(self.now):
		# 	if errorSum >= self.INTEGRAL_ERROR_LIMIT * self.budget:
		# 		if (self.budget - self.timeSpent[i]) > 0:
		# 			continue
		# 	if errorSum <= -self.INTEGRAL_ERROR_LIMIT * self.budget:
		# 		if (self.budget - self.timeSpent[i]) < 0:
		# 			continue
		# 	errorSum += self.budget - self.timeSpent[i]
		# result = errorSum / self.budget
		# if result >= self.INTEGRAL_ERROR_LIMIT:
		# 	return self.INTEGRAL_ERROR_LIMIT
		# if result <= -self.INTEGRAL_ERROR_LIMIT:
		# 	return -self.INTEGRAL_ERROR_LIMIT
		# return errorSum / self.budget