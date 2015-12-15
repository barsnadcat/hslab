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
		#1 do efficient trade - i.e spend your tempo to reduce more enemy tempo
		#2 if enemy kills you faster, reduce it's tempo killing lower creatures with higer creatures
		#3 to the face

		for creature in self.creatures:
			enemy.health -= creature.attack
	
	def IsDead(self):
		return self.health <= 0
		
	def Overdraw():
		self.overdraw += 1
		self.heath -= self.overdraw
		
	