from logging import debug

class Hand:
	def __init__(self):
		self.cards = []
		self.coins = 0
		
	def AddCoins(self, c):
		self.coins += c
		
	def Add(self, card):
		if len(self.cards) + self.coins < 10:
			self.cards.append(card)

	def Play(self, mana):
		#Play opt card
		optCard = 0
		for card in self.cards:
			if card <= mana + self.coins and card > optCard:
				optCard = card
		if optCard > 0:
			self.coins = self.coins - max(optCard - mana, 0)
			self.cards.remove(optCard)
		
		#TODO we need to play more cards if mana allows!
		return optCard
			
