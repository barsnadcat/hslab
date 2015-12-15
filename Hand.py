from logging import debug
from Deck import Deck
class Hand:
	def __init__(self, d):
		self.deck = d
		self.cards = []
		self.coins = 0
		
	def AddCoins(self, c):
		self.coins += c
		
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
		
		return optCard
		
	def Draw(self):
		self.Add(self.deck.TakeRandom())
		
	def Mooligan(self, startCardsCount):
		startHand = [self.deck.TakeRandom() for i in range(startCardsCount)]
		
		for card in startHand:
			if card > 2:
				self.deck.Add(card)
				card = self.deck.TakeRandom()
			self.Add(card)
	
