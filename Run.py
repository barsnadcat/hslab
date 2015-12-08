from Deck import Deck
from Genotype import Genotype
from EvaluateDeck import EvaluateN

population = [Genotype([randint(64) for j in range(9)]) for i in range(1000)]:

for p in population:
	p.fitness = EvaluateN(p.GetDeck(), 1000)