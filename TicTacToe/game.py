# This is the main file which will control the full flow of the Game

from Rules import display_Rule
from player import Player
import Board as brd


def getInfo():
    name = input("\nEnter the name of the player 1 : ")
    sym=''
    while (sym not in ['X','O']):
        sym = input("Enter the symbol of player 1 : ")[0].upper()
    players.append(Player(name,sym))
    name = input("\nEnter the name of the player 2 : ")
    if sym == 'X':
        sym = 'O'
    else:
        sym = 'X'
    players.append(Player(name,sym))
def printWinner(Winner):
    print("\n\nGAME OVER!!")
    print("The Winner is ",Winner.name)

# Main Goes here

display_Rule()
players = []
getInfo()
frame=brd.Board()

for filled in range(9):
    players[filled%2].move(frame)
    if frame.checkWin():
        printWinner(players[filled%2])
        break
else :
    print("\n\nGAME OVER!!")
    print("The Game is a DRAW!! ")
