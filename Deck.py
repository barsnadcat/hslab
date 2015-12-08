from random import randint

class Deck:
	def __init__(self, cards):
		self.cards = cards
		
	def Add(self, card):
		self.cards.append(card)
		
	def TakeRandom(self):
		assert len(self.cards) > 0
		return self.cards.pop(randint(0, len(self.cards) - 1))

		