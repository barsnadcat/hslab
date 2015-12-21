# hslab

In search of perfect manacurve.
Hearthstone tempo\arena prefect mana curve.

Mana curve is function - card count vs card cost. 

With additional limit - 30 cards.

This can be calculated using probability theory, and I've found some one who done it in excel.

I decide to use genetic algorithm to do this. This is basically evristic guided brutforce soulution of optimization problem.

Key decision #1 - gene data format.

And key problem - mutation and crossover opertations, can chage datata in arbitrary way, and they still have to make sense.
I've choosen, simple itegere values that represent quantity of each card.
30 cards per dec limit condition is not enforced on gene data, instead, I do normalization during expression genenome into deck.

Key decision #2 - fitness evaluation function.

First iteration

Assume, that good mana curve is when your average unspent mana is close to 0, while you play 1 card each turn played till turn 7


1 2 3 4 5 6 7

0 6 6 5 5 5 3

Second iteration

Assume, that good mana curve is when your total table tempo is bigger, while you play 1 card each turn, played till turn 7

1 2 3 4 5 6 7

2 7 7 5 5 3 1

With corretion for stdev

1 2 3 4 5 6 7

2 7 7 6 4 3 1

Third iteration

Assume, that good mana curve is when your total table tempo is bigger, while you use all mana each turn, played till turn 7

1 2 3 4 5 6 7

4 9 9 5 2 1 0

Forth iteration

Stop assuming - play full game, use win\lose as survive criteria. 

Simpliphy game - no hero pover, only creatures, with straight stats mana = attack = health.

But implement trade algorithm.

One issue - to evaluate we need deck to play agains

Perfect hand - is one way to do it, but i belive, i will be unbeatable.

Previous generation best deck - current solution. Potentialy may stuck in local optimum.

Found:

1 2 3 4 5 6 7

0 7 7 6 4 3 3

Since there is 3 cards with cost 7, but there is quite some count of cards with stats 8\8 in real game - increase card cost up to 8.

Found

1 2 3 4 5 6 7 8

0 7 7 5 5 4 2 0 

and

1 2 3 4 5 6 7 8

0 7 7 6 4 4 2 0 

and 

1 2 3 4 5 6 7 8

0 6 7 6 5 4 2 0

