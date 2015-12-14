from random import randint
from Deck import Deck
from Curve import Curve

class Genotype:
	def __init__(self, g):
		self.genes = g
		
	def GetCurve(self):
		gs = sum(self.genes)
		
		#all are 0 - it is simplier to return predefined deck
		if gs == 0:		
			return Deck([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9])

		#first approach. Since int rounds down, almost allways sum will be less than 30 cards
		normalized = [int(n * 30 / gs) for n in self.genes]
		
		#Add 1 card at time until we reach 30 cards
		ns = sum(normalized)
		while (ns < 30):					
			diff = [g / gs - n / ns for g, n in zip(self.genes, normalized)]
			index = diff.index(max(diff))
			normalized[index] += 1
			ns = sum(normalized)
				
		return Curve(normalized)
		
		
if __name__ == '__main__':

	g = Genotype([randint(0, 31) for i in range(9)])
	c = g.GetCurve()
	print(c)
	