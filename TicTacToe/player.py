import Board as b

class Player:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol
    
    def move(self,Board):
        Board.show_Board()
        print('\nIts {}\'s Move'.format(self.name))
        idx = None
        while(True):
            idx=int(input("Enter the location Move "))
            
            # print("The move is ", idx)
            
            # if not isinstance(idx, int):
            #     print("Enter the valid Value in Numberical format")
            #     continue
            # # idx=int(idx)
            
            
            if not Board.is_safe(idx-1):
                print("This Place is ALready filled")
                continue
            
            break
        
        Board.update(pos=idx-1,symbol=self.symbol)

        
''' 
# This is the Test of the file        
P=Player("name", 'X')
frame=b.Board()
P.move(frame)
frame.show_Board()
'''    