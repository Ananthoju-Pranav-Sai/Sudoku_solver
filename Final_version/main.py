from cv2 import solve
from sudoku_grab import *
from sudoku_solver import *
from displaysoln import *
from extract_cells import *

img = cv2.imread("sudokus/sudoku2.jpg")
# cap = cv2.VideoCapture(0)
# solved = False
# while(not solved):
try:
    sudoku_img,location = extract_sudoku(img)
    gray = cv2.cvtColor(sudoku_img,cv2.COLOR_BGR2GRAY)
    cells = split_cells(gray)
    board = predict_board(cells)
    # uncomment the below if you want to verify the board
    # print(board)
    mask = np.zeros_like(board)
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                mask[i][j]=1
    game = sudoku()
    game.get_board(board)
    game.solve(0,0)
    solved_mask = (game.board)*mask
    board_mask = np.zeros_like(sudoku_img)
    solved_mask = displaynum(board_mask,solved_mask)
    solved_board = get_INV_perspective(img,solved_mask,location)
    solved_board = cv2.addWeighted(img,0.7,solved_board,1,0)
    cv2.imshow("Solved Board",solved_board)
except:
    print("Cant solve the sudoku either the solution doesn't exist or the sudoku isn't recognised")
    print("Try again")


cv2.imshow("Input Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()