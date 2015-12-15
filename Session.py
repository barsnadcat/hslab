from Curve import Curve
from Hand import Hand
from Board import Board
from Creature import Creature
from random import randint


def Turn(mana, myBoard, enemyBoard, hand, deck):
	card = deck.TakeRandom() 
	if card == None:
		myBoard.Owerdraw()
		if myBoard.IsDead():
			return
	else:
		hand.Add(card)

	myBoard.Attack(enemyBoard)	
	cards = hand.Play(mana)
	myBoard.AddCreatures([Creature(c, c) for c in cards])
	

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
	for i in range(40):
		mana += 1
		if mana > 10:
			mana = 10
		print("*** ", mana, " ***")

			
		Turn(mana, fboard, sboard, fhand, fdeck)

		print(fhand)
		print(fboard)
		print(sboard)
		print(shand)


		if fboard.IsDead():
			return 0
		if sboard.IsDead():
			return 1

		print("--------")

		Turn(mana, sboard, fboard, shand, sdeck)

		print(fhand)
		print(fboard)
		print(sboard)
		print(shand)

		if fboard.IsDead():
			return 0
		if sboard.IsDead():
			return 1
				
	return None
	
if __name__ == '__main__':
	print(Session(Curve([2, 7, 7, 5, 5, 3, 1]).GetDeck(), Curve([2, 7, 7, 6, 4, 3, 1]).GetDeck()))
