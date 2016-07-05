# -*- coding:utf-8 -*-
import time
import random
import numpy as np
from collections import defaultdict

class Simulator(object):
	ALLOCATION_INTERVAL_MEAN = 150
	ALLOCATION_INTERVAL_STDEV = 30
	AFTER_ALLOCATION_INTERVAL_MEAN = 150
	AFTER_ALLOCATION_INTERVAL_STDEV = 30
	CLICK_INTERVAL_MEAN = 30
	CLICK_INTERVAL_STDEV = 20
	OUTPUT_NAME = 'output.csv'
	# Single thread 개발을 위해 time slot 간격으로 나누자.
	# 같은 time slot에 들어온 요청들은 모두 동시 처리 되며 예산 감소도 마찬가지다.
	def __init__(self, budget, unitPrice):
		self.budget = budget
		self.unitPrice = unitPrice
		self.spent = 0
		self.depositRequest = defaultdict(int)
		self.allocationRequest = defaultdict(int)
		self.timeSpent = defaultdict(int)
		self.now = 0
		self.past_spent = 0

	def AdAllocation(self):
		temp = np.random.normal(self.ALLOCATION_INTERVAL_MEAN, self.ALLOCATION_INTERVAL_STDEV, 1)[0]
		if temp < 1:
			requestCount = 0
		else:
			requestCount = int(temp)

		if self.spent > self.budget * 0.9:
			temp = np.random.normal(self.AFTER_ALLOCATION_INTERVAL_MEAN, self.AFTER_ALLOCATION_INTERVAL_STDEV, 1)[0]
			if temp < 1:
				requestCount = 0
			else:
				requestCount = int(temp)

		if requestCount == 0:
			return

		for i in xrange(requestCount):
			isCapped = self.IsCap()
			if isCapped:
				continue
			self.allocationRequest[self.now] += 1
			self.ClickAd()

	def DepositBudget(self):
		self.past_spent = self.spent
		self.spent += self.depositRequest[self.now] * self.unitPrice
		self.timeSpent[self.now] = self.spent
		self.now += 1

	def ClickAd(self):
		interval = np.random.normal(self.CLICK_INTERVAL_MEAN, self.CLICK_INTERVAL_STDEV, 1)[0]
		if interval >= 0:
			clickTime = self.now + int(interval)
		else:
			clickTime = self.now
		self.depositRequest[clickTime] += 1

	def IsCap(self):
		return NotImplemented

	def PrintSpent(self):
		for i in xrange(self.now):
			print str(i) + ',' + str(self.timeSpent[i])

	def PrintAllocation(self):
		allocationSum = 0
		for i in xrange(self.now):
			allocationSum += self.allocationRequest[i]
			print str(i) + ',' + str(allocationSum)

	def OutputResult(self):
		allocationSum = 0
		f = open(self.OUTPUT_NAME, 'w')
		f.write('time,spent,allocation\n')
		for i in xrange(self.now):
			allocationSum += self.allocationRequest[i]
			f.write(str(i) + ',' + str(self.timeSpent[i]) + ',' + str(allocationSum) + '\n')
		f.close()




