from random import randint
from Hand import Hand

class Deck:
	def __init__(self, cards):
		self.cards = cards

	def __str__(self):
		return str(self.cards)
		
	def Add(self, card):
		self.cards.append(card)
		
	def TakeRandom(self):
		if self.cards:
			return self.cards.pop(randint(0, len(self.cards) - 1))
		else:
			return None
			
	def GetHand(self, startCardsCount):
		startHand = [self.TakeRandom() for i in range(startCardsCount)]
		#mooligan
		hand = Hand()
		for card in startHand:
			if card > 2:
				self.Add(card)
				card = self.TakeRandom()
			hand.Add(card)
			
		return hand


		