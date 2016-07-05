# -*- coding:utf-8 -*-
from CurrentSimulator import CurrentSimulator
from PISimulator import PISimulator
from PIDSimulator import PIDSimulator

if __name__ == '__main__':
	budget = 100000
	unitPrice = 8

	currentSimulator = CurrentSimulator(budget=budget, unitPrice=unitPrice)
	piSimulator = PISimulator(budget=budget, unitPrice=unitPrice)
	pidSimulator = PIDSimulator(budget=budget, unitPrice=unitPrice)

	for _ in xrange(1500):
		currentSimulator.AdAllocation()
		currentSimulator.DepositBudget()
		piSimulator.AdAllocation()
		piSimulator.DepositBudget()
		pidSimulator.AdAllocation()
		pidSimulator.DepositBudget()

	currentSimulator.OutputResult()
	piSimulator.OutputResult()
	pidSimulator.OutputResult()