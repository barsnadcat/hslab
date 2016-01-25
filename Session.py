from Curve import Curve
from Deck import Deck
from PerfectDeck import PerfectDeck
from RandomDeck import RandomDeck
from Hand import Hand
from Board import Board
from Creature import Creature
from random import randint



def Turn(mana, myBoard, enemyBoard, hand, deck):
	#print('-----', mana, '-----')
	#print(enemyBoard)
	#print(myBoard)
	#print(hand)
	
	card = deck.TakeRandom()
	#print("Take card ", card)
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
	#print ("Play cards ", cards)

	#Creatures my not fit into the board, play heaviest first
	cards.sort(reverse=True)
	for c in cards:
		if not myBoard.AddCreature(Creature(c, c)):
			hand.Add(c)
			
	myBoard.CalcTotalTempo()

	#print("***Final state***")
	#print(enemyBoard)
	#print(myBoard)
	#print(hand)

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
			return sdeck, sboard.totalTempo
		if sboard.IsDead():
			return fdeck, fboard.totalTempo

		Turn(mana, sboard, fboard, shand, sdeck)

		if fboard.IsDead():
			return sdeck, sboard.totalTempo
		if sboard.IsDead():
			return fdeck, fboard.totalTempo
				
	return None

def Evaluate(curveA, curveB, runs):
	totalAWins = 0
	for i in range(runs):
		deckA = curveA.GetDeck()
		deckB = curveB.GetDeck()
		winner = Session(deckA, deckB)
		totalAWins += int(winner == deckA)

	return totalAWins/runs

def Evaluate2(curve, runs):
	totalAWins = 0
	for i in range(runs):
		deckA = curve.GetDeck()
		deckB = RandomDeck()
		winner, totalTempo = Session(deckA, deckB)
		totalAWins += int(winner == deckA)

	return totalAWins/runs

	
if __name__ == '__main__':

	print("Overdraw")
	myBoard = Board()
	myBoard.health = 1
	enemyBoard = Board()
	deck = Deck([])
	hand = Hand()	
	Turn(10, myBoard, enemyBoard, hand, deck)
	assert(myBoard.health == 0)
	
	
	print("Overpopulate board")
	myBoard = Board([Creature(1, 1), Creature(1, 1), Creature(1, 1), Creature(1, 1), Creature(1, 1), Creature(1, 1)])
	enemyBoard = Board()
	deck = Deck([5, 5, 5, 5, 5, 5])
	hand = Hand()
	hand.Add(4)
	Turn(10, myBoard, enemyBoard, hand, deck)
	assert(len(myBoard.creatures) == 7)
	assert(len(hand.cards) == 1)
	assert(hand.cards[0] == 4)
	
	print("Evaluate2 test")

	print(Evaluate2(Curve([2, 0, 9, 7, 7, 5, 0]), 10000))
	print(Evaluate2(Curve([2, 3, 7, 7, 6, 4, 1]), 10000))
	print(Evaluate2(Curve([0, 6, 7, 6, 5, 4, 2]), 10000))
	print(Evaluate2(Curve([30, 0, 0, 0, 0, 0, 0]), 10000))
	print(Evaluate2(Curve([0, 0, 0, 0, 0, 0, 0, 30]), 10000))
	

	



