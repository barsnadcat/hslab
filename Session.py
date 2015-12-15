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
	
	optCard = hand.Play(mana)
	myBoard.AddCreatures([Creature(optCard, optCard)])
	myBoard.Attack(enemyBoard)
	

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
			
		Turn(mana, fboard, sboard, fhand, fdeck)

		if fboard.IsDead():
			return 0
		if sboard.IsDead():
			return 1

		Turn(mana, sboard, fboard, shand, sdeck)

		if fboard.IsDead():
			return 0
		if sboard.IsDead():
			return 1
				
	return None
	
if __name__ == '__main__':
	print(Session(Curve([2, 7, 7, 5, 5, 3, 1]).GetDeck(), Curve([2, 7, 7, 6, 4, 3, 1]).GetDeck()))
