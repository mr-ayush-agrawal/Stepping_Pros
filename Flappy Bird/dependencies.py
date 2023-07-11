'''
This file is going to have all the dependencies of the mainGame Function
Dependencies here means all the function calls made by the mainGame Function
This shall make the code readablity more
'''

import sys
from load import *
from random import randrange

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


def isCollide(playerx, playery, LowerPipes, UpperPipes):
    '''Returns true on Collidal or going out of the screen'''

    # Checking the Player is in screen or outside
    if playery > BASEY - GAME_IMAGES['bird'].get_height() -2 :
        # At Ground
        GAME_SOUNDS['hit'].play()
        return True
    if playery < 0 :
        # Touches the ceiling
        GAME_SOUNDS['hit'].play()
        return True
    
    pipeHeight =  GAME_IMAGES['pipe'][1].get_height()
    pipeWidth =  GAME_IMAGES['pipe'][1].get_width()
    playerWidth = GAME_IMAGES['bird'].get_width()
    playerHeight = GAME_IMAGES['bird'].get_height()


    # Checking the Pipes hit
    for pipe in UpperPipes :
        if playery < (pipeHeight + pipe['Y']) and ((playerx + playerWidth) >= pipe['X'] and (pipe['X'] + pipeWidth) >= playerx)  :
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in LowerPipes :
        if (playery + playerHeight) > pipe['Y'] and ((playerx + playerWidth) >= pipe['X'] and (pipe['X'] + pipeWidth) >= playerx)  :
            GAME_SOUNDS['hit'].play()
            return True

    return False

