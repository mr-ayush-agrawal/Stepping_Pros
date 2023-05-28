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
    if mode == 2 :
        name = input("\nEnter the name of the player 2 : ")
    else :
        name = 'Computer'

    if sym == 'X':
        sym = 'O'
    else:
        sym = 'X'

    players.append(Player(name,sym))

def printWinner(Winner):
    print("\n\nGAME OVER!!")
    print("The Winner is ",Winner.name)

def getMode():
    print("\nSelect the mode of the game ")
    print("1. Single Player")
    print("2. Multi Player")

    while True:
        try :
            mode=int(input("\nEnter 1/2 Only : "))
            print(mode,type(mode))
            if mode == 1 or mode == 2  :
                return mode
            else :
                continue
        except:
            continue


# Main Goes here

display_Rule()
mode=getMode()
players = []
getInfo()
frame=brd.Board()

for filled in range(9):
    players[filled%2].move(frame,mode)
    if frame.checkWin():
        printWinner(players[filled%2])
        break
else :
    print("\n\nGAME OVER!!")
    print("The Game is a DRAW!! ")
