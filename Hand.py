from SubsetSumSolver import ApproximateSubsetSum

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
		if self.coins:
			s = mana + self.coins
			usedMana, cards = ApproximateSubsetSum(self.cards, s)
			if usedMana == s:
				self.coins = 0
				for card in cards:
					self.cards.remove(card)
				return cards
				
		usedMana, cards = ApproximateSubsetSum(self.cards, mana)		
		for card in cards:
			self.cards.remove(card)
		return cards

