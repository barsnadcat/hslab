from logging import debug
class Hand:
	def __init__(self):
		self.cards = []
		
	def Add(self, card):
		if len(self.cards) < 10:
			self.cards.append(card)

	def Play(self, mana):
		optCard = 0
		for card in self.cards:
			if card <= mana and card > optCard:
				optCard = card
		if optCard > 0:
			self.cards.remove(optCard)
		debug('M %d C %d H %s', mana, optCard, str(self.cards))
		return optCard