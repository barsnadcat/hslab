class Creature:
	def __init__(self, a, h):
		self.attack = a
		self.health = h

	def __str__(self):
		return str(self.attack) + "/" + str(self.health)
