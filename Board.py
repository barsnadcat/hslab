from Creature import Creature

class Board:
	def __init__(self, c=[]):
		self.creatures = c
		self.health = 30
		self.overdraw = 0

	def __str__(self):
		crt = " "
		for c in self.creatures:
			crt += str(c) + " "
		return str(self.health) + crt

		
	def AddCreature(self, c):
		if len(self.creatures) < 7:
			self.creatures.append(c)
			return True
		return False
		
	def Attack(self, enemy):
		#Check if lethal
		totalDamage = 0
		for c in self.creatures:
			totalDamage += c.attack
			if totalDamage >= enemy.health:
				enemy.health = 0
				return

		#Trade up, trade 2 for 1, in other case - face
		myCreatures = SortedCreatures(self.creatures, False)
		enemyCreatures = SortedCreatures(enemy.creatures, True)

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
		

def SortedCreatures(creatures, r):
	res = sorted(creatures, key=lambda c: c.health, reverse=r)
	res.sort(key=lambda c: c.attack, reverse=r)
	return res



if __name__ == '__main__':
	a = Board([Creature(5, 2)])
	b = Board([Creature(2, 2), Creature(2, 1)])
	b.Attack(a)
	assert(b.creatures[0].health == 2)

	a = Board([Creature(5, 2)])
	b = Board([Creature(3, 2), Creature(2, 2)])
	b.Attack(a)
	assert(b.creatures[0].attack == 3)

	a = Board([Creature(5, 1), Creature(5, 2)])
	b = Board([Creature(2, 2)])
	b.Attack(a)
	assert(a.creatures[0].health == 1)

	a = Board([Creature(5, 1), Creature(2, 2)])
	b = Board([Creature(6, 6)])
	b.Attack(a)
	assert(a.creatures[0].attack == 2)

	a = Board([Creature(5, 1)])
	b = Board([Creature(6, 6)])
	a.health = 6
	b.Attack(a)
	assert(a.health == 0)

