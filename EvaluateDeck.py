from Curve import Curve
from Hand import Hand

from random import randint
from statistics import mean, variance
from math import sqrt
from copy import copy

def Evaluate(curve):
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
	for mana in range(1, 9):
		totalTempo += tableTempo
		#draw card
		hand.Add(deck.TakeRandom())

		#play max aviable card
		tableTempo += hand.Play(mana)
		
	return totalTempo
	
def EvaluateN(curve, n):
	res = [Evaluate(curve) for i in range(n)]
	m = mean(res)
	#v = sqrt(variance(res, m))
	return m


if __name__ == '__main__':
	curve = Curve([2, 7, 7, 5, 5, 3, 1])
	print (EvaluateN(curve, 4))
