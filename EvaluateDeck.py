from Deck import Deck
from Hand import Hand

from random import randint

def Evaluate(deck):
	startHand = [deck.TakeRandom() for i in range(3)]
	hand = Hand()
	#mooligan
	for card in startHand:
		if card > 2:
			deck.Add(card)
			card = deck.TakeRandom()
		hand.Add(card)
	
	unusedMana = 0
	for mana in range(1, 11):
		#draw card
		hand.Add(deck.TakeRandom())

		#play max aviable card
		spentMana = hand.Play(mana)
		unusedMana = unusedMana + mana - spentMana
		
	return unusedMana
			

if __name__ == '__main__':
	deck = Deck([randint(1, 10) for i in range(30)])
	print(Evaluate(deck))
