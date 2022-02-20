import numpy as np


temp = np.array([[0,0,0,2,6,0,7,0,1],[6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0],[8,2,0,1,0,0,0,4,0],[0,0,4,6,0,2,9,0,0],[0,5,0,0,0,3,0,2,8],[0,0,9,3,0,0,0,7,4],[0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]])

class sudoku():
    board = np.zeros((9,9))
    def get_board(self,arr):
        self.board = arr

    def is_valid(self,row,col,num):
        for i in range(9):
            if(self.board[row][i]==num):
                return False
        for i in range(9):
            if(self.board[i][col]==num):
                return False
            
        grid_row = row-row%3
        grid_col = col-col%3

        for i in range(3):
            for j in range(3):
                if(self.board[i+grid_row][j+grid_col]==num):
                    return False
        return True
        
    def solve(self,row,col):
        if(row==8 and col==9):
            return True

        if(col==9):
            row+=1
            col=0
        
        if(self.board[row][col]>0):
            return(self.solve(row,col+1))
        
        for i in range(1,10,1):
            if(self.is_valid(row,col,i)):
                self.board[row][col]=i
                if(self.solve(row,col+1)):
                    return True
            self.board[row][col]=0
        return False        

    def print_board(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j],end=' ')
            print()
        

game = sudoku()
game.get_board(temp)
print("Got the board")
game.print_board()
if(game.solve(0,0)):
    print("Solving Complete! Found solution")
    game.print_board()
else:
    print("No Solution !")