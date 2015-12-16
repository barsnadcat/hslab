class Creature:
	def __init__(self, a, h):
		self.attack = a
		self.health = h

	def __str__(self):
		return str(self.attack) + "/" + str(self.health)

	def Melee(self, enemy):
		self.health -= enemy.attack
		enemy.health -= self.attack
