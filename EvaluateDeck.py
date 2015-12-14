from Deck import Deck
from Hand import Hand

from random import randint
from statistics import mean, variance
from math import sqrt
from copy import copy

def Evaluate(d):
	deck = Deck(copy(d.cards))
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
	
	unusedMana = 0
	for mana in range(1, 8):
		#draw card
		hand.Add(deck.TakeRandom())

		#play max aviable card
		spentMana = hand.Play(mana)
		unusedMana = unusedMana + mana - spentMana
		
	return unusedMana
	
def EvaluateN(d, n):
	res = [Evaluate(d) for i in range(n)]
	m = mean(res)
	#v = sqrt(variance(res, m))
	return m


if __name__ == '__main__':
	deck = Deck([max(i % 11, 1) for i in range(30)])
	print (EvaluateN(deck, 4))
