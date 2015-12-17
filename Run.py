from Genotype import Genotype
from Curve import Curve
from Session import Evaluate
from random import randint
from random import random as rand

populationSize = 300
evaluationIteration = 3000
geneMax = 63
cardCostMax = 7
tournamentSize = 4
mutationChance = 0.05
mutationDelta = 10
generationsLimit = 100


def Crossover(father, mother):
	crosspoint = randint(0, len(father.genes) - 1)
	newGenes = []
	for i in range(len(father.genes)):
		if i > crosspoint:
			newGenes.append(father.genes[i])
		else:
			newGenes.append(mother.genes[i])

	return Genotype(newGenes)

def Mutation(p):
	if rand() < mutationChance:
		gene = randint(0, len(p.genes) - 1)
		delta = randint(-mutationDelta, mutationDelta)
		n = max(min(delta + p.genes[gene], geneMax), 0)
		p.genes[gene] = n
	

def Generation(population):
	survivors = []
	bestInTournament = None
	bestInGeneration = population[0]
	for i in range(len(population)):
		p = population[i]
		p.fitness = Evaluate(p.GetCurve(), bestInGeneration.GetCurve(), evaluationIteration)

		if p.fitness > bestInGeneration.fitness:
			bestInGeneration = p

		if bestInTournament:
			if p.fitness > bestInTournament.fitness:
				bestInTournament = p
		else:
			bestInTournament = p
	
		if i % tournamentSize == 0:
			print('Selected ', bestInTournament.fitness, bestInTournament.GetCurve())
			survivors.append(bestInTournament)
			bestInTournament = None
	
	print('Best in generation ', bestInGeneration.fitness, ' ', bestInGeneration.GetCurve())

	survived = len(survivors)
	

	for p in survivors:
		Mutation(p)
	
	died = len(population) - survived
	
	for i in range(died):
		father = randint(0, survived - 1)
		mother = randint(0, survived - 1)
		child = Crossover(survivors[father], survivors[mother])
		survivors.append(child)
	
	return survivors
	
			
population = [Genotype([randint(0, geneMax) for j in range(cardCostMax)]) for i in range(populationSize)]

for i in range(generationsLimit):
	population = Generation(population)

