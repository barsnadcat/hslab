# hslab

In search of perfect manacurve.
Hearthstone tempo\arena prefect mana curve.

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