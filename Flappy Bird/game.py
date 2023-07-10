"""
This contains all the game playing logic.
The game is controlled from the function in the file.
"""

import sys
from load import *
from random import randrange


def mainGame():
    player_Height = GAME_IMAGES['bird'].get_height()
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - player_Height)/2)
    baseX = 0  


    # Creating first 2 pipes for blitting
    newPipe1 = RandPipe()
    newPipe2 = RandPipe()

    # Creating the List of the pipes -> Lower
    LowerPipes = [
        {'X' : SCREENWIDTH + 200, 'Y':newPipe1[0]['Y']},
        {'X' : SCREENWIDTH + 200 + SCREENWIDTH/2, 'Y':newPipe2[0]['Y']}
    ]
    # Creating the List of the pipes -> Upper
    UpperPipes = [
        {'X' : SCREENWIDTH + 200, 'Y':newPipe1[0]['Y']},
        {'X' : SCREENWIDTH + 200 + SCREENWIDTH/2, 'Y':newPipe2[0]['Y']}
    ]

    score = 0
    pipeVelX = -4        # -score*.2 -> Something hit and trial
    




def RandPipe():
    '''
    Generates the position of the pipes and return the list of Dict
    containg the X and Y of the pipes
    '''

    pipeHeight = GAME_IMAGES['pipe'][0].get_height()
    OFFSET = int(SCREENHEIGHT/3) 

    # Generating lower pipe
    y_lower = OFFSET + randrange (0 , int(SCREENHEIGHT - GAME_IMAGES['base'].get_height() - 1.2*OFFSET))
    y_upper = -(pipeHeight - y_lower + OFFSET)
    pipeX = SCREENWIDTH + 15        # It would start from 15 outside the screen

    # List that is to be returned with the co-ordinates

    pipe = [
        {'X' : pipeX, 'Y': y_lower},    # Lower Pipe
        {'X' : pipeX, 'Y': y_upper}     # Upper Pipe
    ]

    return pipe


