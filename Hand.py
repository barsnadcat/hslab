from logging import debug
class Hand:
	def __init__(self):
		self.cards = []
		self.coins = 0
		
	def AddCoins(self, c):
		self.coins = self.coins + c
		
	def Add(self, card):
		if len(self.cards) + self.coins < 10:
			self.cards.append(card)

	def Play(self, mana):
		optCard = 0
		for card in self.cards:
			if card <= mana + self.coins and card > optCard:
				optCard = card
		if optCard > 0:
			self.coins = self.coins - max(optCard - mana, 0)
			self.cards.remove(optCard)
		#debug('M %d C %d H %s %d', mana, optCard, str(self.cards), self.coins)
		return optCard