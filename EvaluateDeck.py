from Deck import Deck
from Hand import Hand

from random import randint
from statistics import mean, variance
from copy import deepcopy
import logging
from logging import debug, info

def Evaluate(d):
	deck = deepcopy(d)
	debug(deck.cards)
	startHand = [deck.TakeRandom() for i in range(3)]
	debug(startHand)
	hand = Hand()
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
			

if __name__ == '__main__':	
	# create logger
	logger = logging.getLogger()
	logger.setLevel(logging.INFO)

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
	res = [Evaluate(deck) for i in range(10000)]
	m = mean(res)
	v = variance(res, m)
	info('%f %f %d %d', m, v, min(res), max(res))
