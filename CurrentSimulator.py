# -*- coding:utf-8 -*-
from Simulator import Simulator
import random

class CurrentSimulator(Simulator):
	PERCENTAGE = 0.01
	BASECAP = 0
	def IsCap(self):
		if random.randrange(100) < self.BASECAP:
			return True
		if self.spent >= self.budget:
			return True
		# if self.spent > self.budget * (1 - self.PERCENTAGE):
		# 	return True
		return False
