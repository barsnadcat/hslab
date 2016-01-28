# hslab
First thing first, here it is:

Now when wannaby legends and newbies have left, lets talk.

Hearthstone tempo\arena prefect mana curve.
Mana curve is function - card count vs card cost. 
With additional limit - 30 cards.

Well, to be honest, I have failed. There is low mana curve - when you run out of cards before your opponent. There is high mana curve when you have nothing to play on early turns. There is good mana curve when you mostly keep your hand with more or same count of cards, and your oponent does not have board advantage. But there is no perfect mana curve. Card quality and synegy are more important in deck composition than mana curve.

Now wneh pro players have left with "I know", let me tell why.

Because Hearthstone is a ****** random game. All those ranks up to legend? They do not show how your skill, nor your deck quality. The just show how many times you have played in ranked, thanks to bonus star effect (http://hearthstone.gamepedia.com/Ranked#Notes).

Now when offended teenagers have left to rebuild their self esteem, let me answer the obivous question, that all smart people had in their mind after reading the headline:
"How did he defined the perfect mana curve?"



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

Yes. There is a problem with previous generation as benchmark - process starts to wobble around optimum - random errors prevenst from futher increase in accuracy. Fighting each other should reduce wobbling a lot.

New iteration - fight each other, so we kill in each generation only halp instead of 75%. Calculate average survived genome instead of selecting best in generation.

To see if computation will not produce anything useful - calculate stdev for each gene value, having it close to mutation on all genes means computation is done.

Apparently low accuracy of comparsion can not push curve futher 0676542, and stdev values stay the same across generations.

Seeding population with previous best curves and increasing accuracy till 20000 had an unexpected turn: new strange looking curve 20977500

Trying seeding again but with a curve values more fitting random generated values. 
I suspect low walues of previously seeded curves prevents mutation from working. It could be solved by gray encoding and bit level mutations.

Better seeding and longer run (200 generations) resulted in new curve 23776410. After checking this curve agains previous one, it is obvious that soulution is drifting, and will unlikly find optimum.

New iteration.

Playing against another deck as evaluation function does not leed us to optimum.
Let's play against perfect hand (hand that plays 1, 2, 3, 4, 5, 6, 7, 8, 4 + 5, 5 + 5).
And fitness will be total temopo.

Result 7, 11, 11, 0, 0, 0, 1, 0, clearly my evaluation function is not what I search for.
Maybe I should limit to 1 card per turn again. Result = 08866200

Perfect hand with total tempo evaluation seems to be step back. Instead play agains random deck and again - use winratio as fitness function. Allow playing multiple cards per turn. Result = 0,11,7,4,3,3,2

What else can be improved? Trading algorithm - you probably should trade equal minions if you are behaind in tempo. Muligan algorithm - you probably should keep one 3 if you are going second.

With fixes to trade algorithm - trade equaly to prevent next turn lethal, and 20000 runs new result is

0,10,7,6,5,2
