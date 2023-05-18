# This is the main program file. This is the only file which is going to contain all the source code for running the game
# The supported files will been imported to keep the code work clean

from words import RandWord 
from functions import *
import Rules
import string
import time

def hangman():
    word = RandWord().upper()
    letters = set(word)                       # All the letters present in the word
    alpha = set(string.ascii_uppercase)       # Contains all the letter A-Z 
    used = set()                              # To store all the letters used by the used
    lives = 7 

    while len(letters) > 0 and lives > 0:
        Outline(lives, used, word)

        user = input("Guess the letter : ")
        user = user[0].upper()                  # In case of multiple input only the first letter would be consider 
        
        # Checking the Enetered letter cetogery
        if user in alpha - used:
            used.add(user)
            if user in letters:
                letters.remove(user)
            else :
                lives-=1
        elif user in used :
            print('The letter ', user, ' is already used before. Try another letter')
        else :
            print('Enter a valid letter')
    
    # Ending the Game
    GameOver(lives)
    print('\nThe word was ', word)


# Also thinking to add the timmer for better experience (time taken to guess the word)
Rules.Rules()
play = True
while play is True :
    start = time.time()
    hangman()
    print('Time took is : ', round(time.time()-start,2), 'sec')
    ch = input('\nDo you want to play again press (Y/y) ')[0]
    if ch in ['Y','y'] :
        pass
    else :
        print('Exiting the Game')
        play = False