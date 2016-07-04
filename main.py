# -*- coding:utf-8 -*-
from CurrentSimulator import CurrentSimulator
from PISimulator import PISimulator

if __name__ == '__main__':
	budget = 150000
	unitPrice = 40

	currentSimulator = CurrentSimulator(budget=budget, unitPrice=unitPrice)
	piSimulator = PISimulator(budget=budget, unitPrice=unitPrice)

	for _ in xrange(7500):
		currentSimulator.AdAllocation()
		currentSimulator.DepositBudget()
		piSimulator.AdAllocation()
		piSimulator.DepositBudget()

	currentSimulator.OutputResult()
	piSimulator.OutputResult()