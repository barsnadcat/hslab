from random import randint
from Hand import Hand
from Genotype import cardCostMax

class RandomDeck:
	def __init__(self):
		self.cards = 30

	def __str__(self):
		return str(self.cards)
		
	def Add(self, card):
		pass
		
	def TakeRandom(self):
		if self.cards > 0:
			self.cards -= 1
			return randint(1, cardCostMax)
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


		