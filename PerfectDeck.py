
class PefectHand:
	def __str__(self):
		return "Perfect hand"
		
	def AddCoins(self, c):
		pass
		
	def Add(self, card):
		pass

	def Play(self, mana):
		if mana < 9:
			return [mana]
		elif mana == 9:
			return [4, 5]
		else:
			return [5, 5]

class PerfectDeck:
	def __init__(self):
		self.cards = 30

	def __str__(self):
		return "Perfect " + str(self.cards)
		
	def Add(self, card):
		self.cards += 1
		
	def TakeRandom(self):
		if self.cards > 0:
			self.cards -= 1
			return 1
		else:
			return None
			
	def GetHand(self, startCardsCount):			
		return PefectHand()