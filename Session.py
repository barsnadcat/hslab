from Curve import Curve
from Deck import Deck
from Hand import Hand
from Board import Board
from Creature import Creature
from random import randint


def Turn(mana, myBoard, enemyBoard, hand, deck):
	card = deck.TakeRandom() 
	if card == None:
		myBoard.Overdraw()
		if myBoard.IsDead():
			return
	else:
		hand.Add(card)

	myBoard.Attack(enemyBoard)	

	if enemyBoard.IsDead():
		return

	cards = hand.Play(mana)

	#Creatures my not fit into the board, play heaviest first
	cards.sort(reverse=True)
	for c in cards:
		if not myBoard.AddCreature(Creature(c, c)):
			hand.Add(c)

	

def Session(deckA, deckB):
	fdeck = deckA
	sdeck = deckB
	
	if randint(0, 1):
		fdeck, sdeck = sdeck, fdeck
		
	fhand = fdeck.GetHand(3)
	shand = sdeck.GetHand(4)
	shand.AddCoins(1)
	
	fboard = Board()
	sboard = Board()
	
	mana = 0
	for i in range(50):
		mana += 1
		if mana > 10:
			mana = 10
			
		Turn(mana, fboard, sboard, fhand, fdeck)

		if fboard.IsDead():
			return sdeck
		if sboard.IsDead():
			return fdeck

		Turn(mana, sboard, fboard, shand, sdeck)

		if fboard.IsDead():
			return sdeck
		if sboard.IsDead():
			return fdeck
				
	return None

def Evaluate(curveA, curveB, runs):
	totalAWins = 0
	for i in range(runs):
		deckA = curveA.GetDeck()
		deckB = curveB.GetDeck()
		winner = Session(deckA, deckB)
		totalAWins += int(winner == deckA)

	return totalAWins/runs
	
if __name__ == '__main__':

	#Overdraw
	myBoard = Board()
	myBoard.health = 1
	enemyBoard = Board()
	deck = Deck([])
	hand = Hand()	
	Turn(10, myBoard, enemyBoard, hand, deck)
	assert(myBoard.health == 0)
	
	
	#Overpopulate board
	myBoard = Board([Creature(1, 1), Creature(1, 1), Creature(1, 1), Creature(1, 1), Creature(1, 1), Creature(1, 1)])
	enemyBoard = Board()
	deck = Deck([5, 5, 5, 5, 5, 5])
	hand = Hand()
	hand.Add(4)
	Turn(10, myBoard, enemyBoard, hand, deck)
	assert(len(myBoard.creatures) == 7)
	assert(len(hand.cards) == 1)
	assert(hand.cards[0] == 4)
	
	
	print(Evaluate(Curve([2, 7, 7, 5, 5, 3, 1]), Curve([2, 7, 7, 5, 5, 3, 1]), 5000))

	



