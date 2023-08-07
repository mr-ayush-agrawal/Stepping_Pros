import Rules

def showBoard(board):
    print("The current state of the board is\n")
    for i in range (9):
        if i%3 == 0 :
            print()     
        if not board[i]:
            print("_",end="  ")
        elif board[i] == -1:
            print('X',end="  ")
        else :
            print("O",end="  ")
    print("\n")

def U1Turn(board):
    pos = int(input("Enetr the X's Postion from 1-9 : "))- 1
    if board[pos] :
        print("Wrong Move !!!")
        exit(0)
        # Exiting the program when the input is wrong
    board[pos]= -1

def U2Turn(board):
    pos = int(input("Enetr the 0's Postion from 1-9 : "))- 1
    if board[pos] :
        print("Wrong Move !!!")
        exit(0)
        # Exiting the program when the input is wrong
    board[pos]= 1


def Win(board):

    # Horizontal
    for i in range(0,9,3):
        if board[i]==board[i+1] and board[i]== board[i+2] and board[i] != 0:
            # print(i,'Horizontal')
            return board[i]

    # Vertical
    for i in range(0,3):
        if board[i]==board[i+3] and board[i]== board[i+6] and board[i] != 0:
            # print(i,'Vertical')
            return board[i]

    # Diagonals
    if board[0]==board[4] and board[0]== board[8] and board[4] != 0:
        # print(i,'Dia 1')
        return board[i]
    elif board[2]==board[4] and board[2]== board[6] and board[4] != 0:
        # print(i,'Dia 2')
        return board[i]
        
    return 0


if __name__ =='__main__':
    Rules.display_Rule()    
    ch = int(input("Enter 1 for 1 playrer else 2 for 2 players "))
    board = [0 for x in range(1,10)]
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
            if i%2 == 0:
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
        print("Player X wins!! and O looses")
    else :
        showBoard(board)
        print("Player O wins!! and X looses")