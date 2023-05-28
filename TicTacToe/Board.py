class Board:
    def __init__(self):
        self.__locs =[" " for i in range(9)]
        
    def update(self,pos,symbol):
        self.__locs[pos]=symbol
        
    def show_Board(self):
        print('\n')
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(self.__locs[0],self.__locs[1],self.__locs[2]))
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(self.__locs[3],self.__locs[4],self.__locs[5]))
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print("  {}  |  {}  |  {}  ".format(self.__locs[6],self.__locs[7],self.__locs[8]))
        print("     |     |     ")
        print()
        
    def is_safe(self,idx):
        if self.__locs[idx]==" ":
            return True
        else :
            return False
        
    def checkWin(self):
        # Horizontal
        for i in range(0,9,3):
            if self.__locs[i]==self.__locs[i+1] and self.__locs[i]== self.__locs[i+2] and self.__locs[i] != ' ':
                print(i,'Horizontal')
                return True
        
        # Vertical
        for i in range(0,3):
            if self.__locs[i]==self.__locs[i+3] and self.__locs[i]== self.__locs[i+6] and self.__locs[i] != ' ':
                print(i,'Vertical')
                return True
        
        # Diagonals
        if self.__locs[0]==self.__locs[4] and self.__locs[0]== self.__locs[8] and self.__locs[4] != ' ':
            print(i,'Dia 1')
            return True
        elif self.__locs[2]==self.__locs[4] and self.__locs[2]== self.__locs[6] and self.__locs[4] != ' ':
            print(i,'Dia 2')
            return True
           
        return False