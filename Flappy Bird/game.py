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
    
    playerVelY = -9 
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1
    playerFlapAccV = -8
    playerFlapped = False

    # Making the main game loop
    while True :
        for events in event.get():
            if events.type == QUIT or (events.type == KEYDOWN and events.key == K_ESCAPE) :
                pygame.quit()
                sys.exit()
            elif events.type == KEYDOWN and (events.key == K_SPACE or events.key == K_UP) :
                # UPdating the variables in the game
                if playery > 0 : 
                    # Inside the screen
                    playerFlapped = True
                    playerAccY = playerFlapAccV
                    GAME_SOUNDS['wing'].play()

        # Check for the collidial
        if isCollide(playerx, playery, LowerPipes, UpperPipes) :
            return

        # Check for the score.
        playerMidPos = playerx + GAME_IMAGES['bird'].get_width()/2
        # For upper pipes
        for pipe in UpperPipes :
            pipeMidPos = pipe['X'] + GAME_IMAGES['pipe'].get_width()/2

            # Setting up the condition for checking the position of player 
            if pipeMidPos <= playerMidPos <pipeMidPos + 4:
                score+=1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()

        # Updating the player velocity if not flapper
        if playerVelY < playerMaxVelY and not playerFlapped :
            playerVelY += playerAccY

        elif playerFlapped :
            playerFlapped = False

        playery = playery + min(playery, BASEY - playery - player_Height)

        # Moving the pipes to left
        for Upper , Lower in zip (UpperPipes, LowerPipes):
            Upper['X'] += pipeVelX
            Lower['X'] += pipeVelX

        # Adding a new pipe when the pipe is about to get remove
        if 0 < UpperPipes[0]['X'] < 10:
            newPipe = RandPipe()
            UpperPipes.append(newPipe[1])
            LowerPipes.append(newPipe[0])
            # Here 0 , 1 are according to return val of the RandPipe

        # Removing the pipe if outside the screen
        if UpperPipes[0]['X'] < -GAME_IMAGES['pipe'].get_width() :
            UpperPipes.pop(0)
            LowerPipes.pop(0)
            # 0 are the index of first pipe in the flow

        # Now blitting the sprites on the screen
        SCREEN.blit(GAME_IMAGES['background'], (0, 0))
            # Blitting the Pipes
        for Upper , Lower in zip (UpperPipes, LowerPipes):
            SCREEN.blit(GAME_IMAGES['pipe'][0], (Upper['X'], Upper['Y']))
            SCREEN.blit(GAME_IMAGES['pipe'][1], (Lower['X'], Lower['Y']))
            
        SCREEN.blit(GAME_IMAGES['base'], (baseX, BASEY))
        SCREEN.blit(GAME_IMAGES['player'], (playerx, playery))



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
    pass