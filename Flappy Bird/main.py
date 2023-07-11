from game import *

def welcomeScreen() :
    '''
    Shows the welcome Images on the screen.
    There can be any welcome Image for the game Here I am just gonna use the Background Image only which can be changed on later development of the game
    You just have to press SpaceBar or the Up Arrow Key to start the game.
    '''
    player_Height = GAME_IMAGES['bird'].get_height()
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - player_Height)/2)

    baseX = 0

    while True :
        for events in event.get() :
            # Esc / X(button) -> Exit the game
            if (events.type == QUIT) or (events.type == KEYDOWN and events.key == K_ESCAPE) :
                # Quitting and exiting the Game
                pygame.quit()
                sys.exit()
            # Starting the game if -> Space or Up
            elif events.type == KEYDOWN and (events.key == K_SPACE or events.key==K_UP) :
                # Start the Game -> If we return the mainGame funcion Executes
                return
            # Blitting the images
            else :
                SCREEN.blit(GAME_IMAGES['background'],(0,0))
                SCREEN.blit(GAME_IMAGES['bird'],(playerx,playery))
                SCREEN.blit(GAME_IMAGES['base'],(baseX,BASEY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

    
# ***Srating I have to move it to main of game.py ***

loadImages()        # Loading the images form the system to program
loadSounds()        # Loading Sound files


# This is now the main while loop which will be executed to start the game each time
while True :
    welcomeScreen()     # Function to start the game
    mainGame()          # Where all the logic of the game is written