from termcolor import colored, cprint

def GameOver(lives) :
    if  lives == 0 :
        cprint('\n\nSORRY NO LIVES LEFT, YOU DIED !!! ', 'red')
    else :
        cprint('\n\nYou have sucessfully guessed the letter', 'green')
         
def Outline(lives, used, word):
    print('\n\n')

    print('You have ', end='')
    cprint(lives, 'red', attrs=['bold'], end='')
    print(' lives left ')
    
    
        # Printing the guessed Letters
    print('Used Letter : ', end='')
    cprint(' '.join(sorted(used)), 'light_red' )
    
        # Printing the status of the word
    current = [i if i in used else '_' for i in word ]
    print('The Word : ' , end= '')
    cprint(' '.join(current), 'green')
        