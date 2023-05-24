
# board = [
#  ["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,["9",".",".","4","1","9",".","","5"]
# ,[".",".",".",".","8",".",".","7","9"]]


board = [
 [".",".","." ,".","5",".", ".",".","."],
 [".","4","." ,".",".",".", ".",".","."],
 [".",".","." ,".",".","3", ".",".","1"],

 ["8",".","." ,".",".",".", ".","2","."],
 [".",".","2" ,".","7",".", ".",".","."],
 [".","1","5" ,".",".",".", ".",".","."],

 [".",".","." ,".",".","2", ".",".","."],
 [".","2","." ,"9",".",".", ".",".","."],
 [".",".","4" ,".",".",".", ".",".","."]]
print("len of board",len(board))


def sudoku(board):
    # flag = 0

    # for rows.
    for i in range(len(board)):
        lsit = []
        for j in board[i]:

            if j == ".":
                continue
            if j in lsit:
                 return False

            else:
                lsit.append(j)
        # print(lsit)

    # for columns
    for i in range(len(board)):
        lsit = []
        for j in range(len(board)):
            if board[j][i] == ".":
                continue
            if board[j][i] in lsit:
                return False
            else:                
                lsit.append(board[j][i])
        # print("list is ",lsit)


    # for 3 X 3 
    for i in range(0,len(board),3):
        for j in range(0,len(board),3):
            sub_list  = []
            for k in range(0,3):
                    for l in range(0,3):
                        if board[k+i][l+j] == ".":
                              continue

                        if board[k+i][l+j] in sub_list:
                              
                              return(False)
                        
                        else:
                              sub_list.append(board[k+i][l+j])

                        print(k+i,l+j)
                        
            print("...................",sub_list)     
        




p = sudoku(board)
print(p)
# flag = 0
# for i in range(0,len(board),3):
#         for j in range(0,len(board),3):
#             sub_list  = []
#             for k in range(0,3):
#                     for l in range(0,3):
#                         if board[k+i][l+j] == ".":
#                               continue

#                         if board[k+i][l+j] in sub_list:
#                               flag = 1
#                               break
#                         else:
#                               sub_list.append(board[k+i][l+j])

#                         # print(board[k+i][l+j])
                        
#             print("...................",sub_list)    

   
# print("count is" ,count)