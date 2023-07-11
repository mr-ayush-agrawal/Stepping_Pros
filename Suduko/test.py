import PrintBoard as pb
from Board import Board
from SoloveBoard import SolveBoard
# from SoloveBoard import isValid


print("Before solving")
pb.Show(Board)
SolveBoard(Board)
# print(type(Board))
# print(Board)
# if Board is True :
print("After solving")
pb.Show(Board)

# B =[[8,0,0,6,0,0,0,0,0],
#         [0,2,0,0,0,0,9,0,0],
#         [9,0,0,0,1,7,0,0,8],
#         [0,5,0,0,7,4,0,1,0],
#         [0,0,0,2,0,0,0,0,4],
#         [7,0,0,6,0,0,0,0,0],
#         [2,0,0,0,9,8,0,0,1],
#         [0,0,3,0,0,0,0,5,0],
#         [0,0,0,4,0,0,0,0,0]]

# pb.Show(B)
# print(isValid(B,7,4,2))