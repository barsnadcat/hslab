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
	startHand = [deck.TakeRandom() for i in range(3 + secondTurn)]
	hand = Hand()
	hand.AddCoins(secondTurn)

	#mooligan
	for card in startHand:
		if card > 2:
			deck.Add(card)
			card = deck.TakeRandom()
		hand.Add(card)
	
	totalTempo = 0
	tableTempo = 0
	for mana in range(1, turns + 1):
		totalTempo += tableTempo
		#draw cardr
		hand.Add(deck.TakeRandom())

		#play max aviable card
		tableTempo += hand.Play(mana)
		
	return totalTempo
	
def EvaluateN(curve, n, t):
	res = [Evaluate(curve, t) for i in range(n)]
	m = mean(res)
	v = sqrt(variance(res, m))
	return Fitness(m, v)


if __name__ == '__main__':
	print (EvaluateN(Curve([2, 6, 7, 6, 4, 4, 1]), 100000, 8))
	print (EvaluateN(Curve([2, 7, 7, 5, 5, 3, 1]), 100000, 8))	
	print (EvaluateN(Curve([2, 7, 7, 6, 4, 3, 1]), 100000, 8))

