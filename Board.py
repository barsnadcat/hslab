class Board:
	def __init__(self):
		self.creatures = []
		self.health = 30
		self.overdraw = 0

	def __str__(self):
		crt = " "
		for c in self.creatures:
			crt += str(c) + " "
		return str(self.health) + crt

		
	def AddCreatures(self, cs):
		self.creatures.extend(cs)
		
	def Attack(self, enemy):
		#logic of attack
		# 0 if letal - go to face
		# 1 trade
		# 1 For each my creature, starting from creatures with lower attack:
		# 1.1 Find strongest enemy creatures with not full healt to kill
		# 1.2 Or find the strongest enemy creatures to kill without losing creature
		# 1.3 if none - to the face

		for creature in self.creatures:
			enemy.health -= creature.attack
	
	def IsDead(self):
		return self.health <= 0
		
	def Overdraw():
		self.overdraw += 1
		self.heath -= self.overdraw
		
	