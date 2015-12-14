
from Deck import Deck

class Curve:
	def __init__(self, c):
		self.costs = c

	def __str__(self):
		return str(self.costs)

	def GetDeck(self):
		cards = []
		for manaCost in range(len(self.costs)):
			count = self.costs[manaCost]
			for i in range(count):
				cards.append(manaCost + 1)
		return Deck(cards)