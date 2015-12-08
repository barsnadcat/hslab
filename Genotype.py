from random import randint
from Deck import Deck

class Genotype:
	def __init__(self, g):
		self.genes = g
		
	def GetDeck(self):
		s = sum(self.genes)
		normalized = [n * 30 / s for n in self.genes]		
		print(normalized)
		cards = []
		for manaCost in range(len(normalized)):
			count = int(normalized[manaCost])
			for i in range(count):
				cards.append(manaCost + 1)
		return Deck(cards)
		
		
if __name__ == '__main__':
	g = Genotype([1 for i in range(9)])
	d = g.GetDeck()
	print(d.cards, ' ', len(d.cards))