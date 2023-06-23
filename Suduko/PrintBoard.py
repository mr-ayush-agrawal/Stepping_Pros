def Show(Board):
    for i in range (9) :
        if i%3==0 :
            print('------------------------')
        for j in range (9):
            if j%3==0 :
                print('|',end=' ')
            if Board[i][j] == 0 :
                print(" ", end=' ')
            else :
                print(Board[i][j], end=' ')
        
        print('|',end=' ')
        print()

        
    print('------------------------')
    