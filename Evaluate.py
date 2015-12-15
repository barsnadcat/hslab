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
	hand = Hand(deck)
	hand.Mooligan(3 + secondTurn)
	hand.AddCoins(secondTurn)
	
	totalTempo = 0
	tableTempo = 0
	for mana in range(1, turns + 1):
		hand.Draw()
		#play max aviable card
		tableTempo += hand.Play(mana)
		totalTempo += tableTempo
		
	return totalTempo
	
def EvaluateN(curve, n, t):
	res = [Evaluate(curve, t) for i in range(n)]
	m = mean(res)
	v = sqrt(variance(res, m))
	return Fitness(m, v)


if __name__ == '__main__':
	print (EvaluateN(Curve([2, 8, 7, 6, 4, 2, 1]), 1000000, 7))
	print (EvaluateN(Curve([2, 7, 7, 5, 5, 3, 1]), 1000000, 7))	
	print (EvaluateN(Curve([2, 7, 7, 6, 4, 3, 1]), 1000000, 7))

	
	#logic of attack
	#1 do efficient trade - i.e spend your tempo to reduce more enemy tempo
	#2 if enemy kills you faster, reduce it's tempo killing lower creatures with higer creatures
	#3 to the face
