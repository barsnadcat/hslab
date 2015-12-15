from Curve import Curve
from Fitness import Fitness
from Hand import Hand

from random import randint
from statistics import mean, variance
from math import sqrt
from copy import copy

def Evaluate(curve, turns):
	deck = curve.GetDeck()

	secondTurn = randint(0, 1)
	hand = deck.GetHand(3 + secondTurn)
	hand.AddCoins(secondTurn)
	
	totalTempo = 0
	tableTempo = 0
	for mana in range(1, turns + 1):
		card = deck.TakeRandom() 
		hand.Add(card)
		
		#play max aviable card
		tableTempo += sum(hand.Play(mana))
		totalTempo += tableTempo
		
	return totalTempo
	
def EvaluateN(curve, n, t):
	res = [Evaluate(curve, t) for i in range(n)]
	m = mean(res)
	v = sqrt(variance(res, m))
	return Fitness(m, v)


if __name__ == '__main__':
	print (EvaluateN(Curve([2, 8, 7, 6, 4, 2, 1]), 100000, 7))
	print (EvaluateN(Curve([2, 7, 7, 5, 5, 3, 1]), 100000, 7))	
	print (EvaluateN(Curve([2, 7, 7, 6, 4, 3, 1]), 100000, 7))
	print (EvaluateN(Curve([4, 9, 9, 5, 2, 1, 0]), 100000, 7))

	
