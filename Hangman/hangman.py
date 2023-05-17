# This is the main program file. This is the only file which is going to contain all the source code for running the game
# The supported files will been imported to keep the code work clean

from words import RandWord 
import string

def hangman():
    word = RandWord().upper()
    letters = set(word)                       # All the letters present in the word
    alpha = set(string.ascii_uppercase)       # Contains all the letter A-Z 
    used = set()                              # To store all the letters used by the used
    lives = 6 

    while len(letters) > 0 and lives > 0:
        print('\n\n')
        # Formating the ouput sreen
        print('You have ',lives,' lives left ')
            # Printing the guessed Letters
        print('Used Letter : ', ' '.join(sorted(used)))
            # Printing the status of the word
        current = [i if i in used else '_' for i in word ]
        print('The Word : ' , ' '.join(current))
        
        # Accepting letter form the user 
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
    
    if  lives == 0 :
        print('\n SORRY NO LIVES LEFT, YOU DIED !!! ')
    else :
        print('You have sucessfully guessed the letter')
        
    print('The word was ',word)



# Thinking to add a rule page at the bening of the game
# Also thinking to add the timmer for better experience (time taken to guess the word)
hangman()