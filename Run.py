from Genotype import Genotype
from Curve import Curve
from Session import Evaluate2
from random import randint
from random import random as rand
from math import sqrt
import sys

populationSize = 200
evaluationIteration = 20000
geneMax = 63
cardCostMax = 8
tournamentSize = 4
mutationChance = 0.05
mutationDelta = 10
generationsLimit = 1000


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
	
	averageGenome = [0 for i in range(cardCostMax)]
	bestInTournament = None
	bestInGeneration = None
	for i in range(len(population)):
		p = population[i]
		p.fitness = Evaluate2(p.GetCurve(), evaluationIteration)
		
		if bestInGeneration:
			if p.fitness > bestInGeneration.fitness:
				bestInGeneration = p
		else:
			bestInGeneration = p

		if bestInTournament:
			if p.fitness > bestInTournament.fitness:
				bestInTournament = p
		else:
			bestInTournament = p
	
		if i % tournamentSize == 0:
			print(int(i/populationSize * 100), ' Selected ', int(bestInTournament.fitness * 100), bestInTournament.GetCurve())
			sys.stdout.flush()
			survivors.append(bestInTournament)
			for i in range(cardCostMax):
				averageGenome[i] += bestInTournament.genes[i]
			bestInTournament = None
			
	print('Best in generation ', bestInGeneration.fitness, ' ', bestInGeneration.GetCurve())
	print('Average curve ', Genotype(averageGenome).GetCurve())
	for i in range(cardCostMax):
		sum = 0;
		for s in survivors:
			sum += s.genes[i]
		mean = sum / populationSize / 2
		variance = 0
		for s in survivors:
			v = s.genes[i] - mean
			variance += v * v
		stdev = sqrt(variance / populationSize / 2)
		
		print(i, ": ", mean, "(+/- ", stdev, ")")
	sys.stdout.flush()
		

	survived = len(survivors)
	

	for p in survivors:
		Mutation(p)
	
	died = populationSize - survived
	
	for i in range(died):
		father = randint(0, survived - 1)
		mother = randint(0, survived - 1)
		child = Crossover(survivors[father], survivors[mother])
		survivors.append(child)
	
	return survivors
	
			
population = [Genotype([randint(0, geneMax) for j in range(cardCostMax)]) for i in range(populationSize)]

for i in range(10):
	population[randint(0, populationSize-1)].genes = [0, 6 * 4, 7 * 4, 6 * 4, 5 * 4, 4 * 4, 2 * 4, 0]

for i in range(10):
	population[randint(0, populationSize-1)].genes = [0, 7 * 4, 7 * 4, 5 * 4, 5 * 4, 4 * 4, 2 * 4, 0]

for i in range(10):
	population[randint(0, populationSize-1)].genes = [0, 7 * 4, 7 * 4, 6 * 4, 4 * 4, 4 * 4, 2 * 4, 0]
	
for i in range(10):
	population[randint(0, populationSize-1)].genes = [2 * 4, 0, 9 * 4, 7 * 4, 7 * 4, 5 * 4, 0, 0]



for i in range(generationsLimit):
	print('Generation ', i)
	population = Generation(population)

