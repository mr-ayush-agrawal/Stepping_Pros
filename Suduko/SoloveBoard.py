def isValid (Board, i,j,num):
    for x in range (9):
        if Board[i][x]==num or Board[x][j]==num:
            return False
    
    RQ=i//3
    CQ=j//3
    for x in range(3):
        for y in range(3):
            if Board[RQ*3+x][CQ*3+y]==num :
                return False
    
    return True

def SolveBoard(Board):
    for i in range (9):
        for j in range(9):
            if Board[i][j] == 0 :
                for nxt in range (1,10):
                    if isValid(Board, i, j, nxt) :
                        Board[i][j]=nxt
                        SolveBoard(Board)
                        if SolveBoard :
                            return True
                        else :
                            Board[i][j]=0
                return False
    return True