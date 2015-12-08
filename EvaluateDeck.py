from Deck import Deck
from Hand import Hand

from random import randint
from statistics import mean, variance
from math import sqrt
from copy import deepcopy
import logging
from logging import debug, info

def Evaluate(d):
	deck = deepcopy(d)
	debug(deck.cards)
	secondTurn = randint(0, 1)
	startHand = [deck.TakeRandom() for i in range(3 + secondTurn)]
	debug(startHand)
	hand = Hand()
	hand.AddCoins(secondTurn)
	#mooligan
	for card in startHand:
		if card > 2:
			deck.Add(card)
			card = deck.TakeRandom()
		hand.Add(card)
	
	unusedMana = 0
	for mana in range(1, 9):
		#draw card
		hand.Add(deck.TakeRandom())

		#play max aviable card
		spentMana = hand.Play(mana)
		unusedMana = unusedMana + mana - spentMana
		
	return unusedMana
	
def EvaluateN(d, n):
	res = [Evaluate(deck) for i in range(n)]
	m = mean(res)
	v = sqrt(variance(res, m))
	debug('%f %f %d %d', m, v, min(res), max(res))
	return m


if __name__ == '__main__':	
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)

	# create console handler and set level to debug
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	# create formatter
	formatter = logging.Formatter('%(message)s')
	# add formatter to ch
	ch.setFormatter(formatter)
	# add ch to logger
	logger.addHandler(ch)
		
	
	deck = Deck([max(i % 11, 1) for i in range(30)])
	print (EvaluateN(deck, 4))
