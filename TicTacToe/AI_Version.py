import Rules










if __name__ =='__main__':
    Rules.display_Rule()    
    ch = int(input("Enter 1 for 1 playrer else 2 for 2 players "))
    board = [x for x in range(1,10)]
    print(board)

    if ch ==1 :
        print("Its Computer : O Vs You : X")
        player = int(input("You want to play 1st or 2nd"))
        for i in range(9):
            if(Win(board)):
                break

            # i + player == 0 -> Chance of AI 
            if (i+player)%2 == 0:
                compTurn(board)
            else :
                showBoard(board)
                U1Turn(board)
    
    # Else part is for the multiplayer
    else :
        for i in range(9):
            if(Win(board)):
                break

            # i + player == 0 -> Chance of AI 
            if (i+player)%2 == 0:
                showBoard(board)
                U1Turn(board)
            else :
                showBoard(board)
                U2Turn(board)

    # Printing the WInnwe
    winner = Win(board)
    if (winner == 0):
        showBoard(board)
        print("Its a Draw!!")
    elif (winner == -1) :
        showBoard(board)
        print("Player X wins!! and O looses")8
    else :
        showBoard(board)
        print("Player O wins!! and X looses")