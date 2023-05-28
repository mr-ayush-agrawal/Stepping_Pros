
import random as rd
import time as t

class Player:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol
    
    def move(self,Board,mode):
        Board.show_Board()
        print('\nIts {}\'s Move'.format(self.name))
        idx = None
        while(True):
            # Setting Computers move in auto mode
            if mode==1 and self.name=='Computer':
                while True :
                    idx = rd.randint(1,10) 
                    if not Board.is_safe(idx-1):
                        continue
                    else :
                        print("Computer is Playing at ",idx)
                        t.sleep(2.5)
                        break
                break

            try:
                idx=int(input("Enter the location Move "))
            except:
                print("Enter the valid Value in Numberical format")
                continue

            if not Board.is_safe(idx-1):
                print("This Place is ALready filled")
                continue
            
            break
        
        Board.update(pos=idx-1,symbol=self.symbol)

        
''' 
This is the Test of the file        
P=Player("Computer", 'X')
frame=b.Board()
P.move(frame,1)
frame.show_Board()
'''