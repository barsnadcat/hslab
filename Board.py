from Creature import Creature

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
		#Check if lethal
		totalDamage = 0
		for c in self.creatures:
			totalDamage += c.attack
			if totalDamage >= enemy.health:
				enemy.health = 0
				return

		#Trade up, trade 2 for 1, in other case - face
		myCreatures = SortMyCreatures(self.creatures)
		enemyCreatures = SortEnemyCreatures(enemy.creatures)

		myAliveCreatures = []
		for mc in myCreatures:

			target = None
			for ec in enemyCreatures:
				if mc.attack >= ec.health and (ec.attack > mc.attack or mc.health > ec.attack):
					target = ec
					break

			if target:
				mc.Melee(target)
				#It should be dead - we do not attack if we can not kill
				enemyCreatures.remove(target)
			else:
				enemy.health -= mc.attack

			#We can not just remove it from myCreatures, since we iterating over it
			if mc.health >= 0:
				myAliveCreatures.append(mc)

		enemy.creatures = enemyCreatures
		self.creatures = myAliveCreatures

	
	def IsDead(self):
		return self.health <= 0
		
	def Overdraw():
		self.overdraw += 1
		self.heath -= self.overdraw
		

def SortEnemyCreatures(creatures):
	res = sorted(creatures, key=lambda c: 10 - c.health)
	res.sort(key=lambda c: 10 - c.attack)
	return res

def SortMyCreatures(creatures):
	res = sorted(creatures, key=lambda c: c.health)
	res.sort(key=lambda c: c.attack)
	return res


#TODO limit board space

if __name__ == '__main__':
	a = Board()
	b = Board()
	a.AddCreatures([Creature(5, 2)])
	b.AddCreatures([Creature(2, 2), Creature(2, 1)])
	b.Attack(a)
	assert(b.creatures[0].health == 2)

	a = Board()
	b = Board()
	a.AddCreatures([Creature(5, 2)])
	b.AddCreatures([Creature(3, 2), Creature(2, 2)])
	b.Attack(a)
	assert(b.creatures[0].attack == 3)

	a = Board()
	b = Board()
	a.AddCreatures([Creature(5, 1), Creature(5, 2)])
	b.AddCreatures([Creature(2, 2)])
	b.Attack(a)
	assert(a.creatures[0].health == 1)

	a = Board()
	b = Board()
	a.AddCreatures([Creature(5, 1), Creature(2, 2)])
	b.AddCreatures([Creature(6, 6)])
	b.Attack(a)
	assert(a.creatures[0].attack == 2)

	a = Board()
	b = Board()
	a.AddCreatures([Creature(5, 1)])
	a.health = 6
	b.AddCreatures([Creature(6, 6)])
	b.Attack(a)
	assert(a.health == 0)

