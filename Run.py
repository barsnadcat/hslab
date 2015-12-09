from Deck import Deck
from Genotype import Genotype
from EvaluateDeck import EvaluateN
from random import randint

populationSize = 1000
evaluationIteration = 200
geneMax = 64
cardCostMax = 9


population = [Genotype([randint(0, geneMax) for j in range(cardCostMax)]) for i in range(populationSize)]

minFitness = 999
best = None
for p in population:
	p.fitness = EvaluateN(p.GetDeck(), evaluationIteration)
	if best:
		if p.fitness < best.fitness:
			best = p
			print(p.fitness)
	else:
		best = p

print(best.GetDeck().cards)
		
	