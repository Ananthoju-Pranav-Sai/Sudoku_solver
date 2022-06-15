# Sudoku_solver
Solving sudoku using opencv and backtracking algorithm.

Final version of the program is contained in "/Final_version"

## Prerequisites :
1. opencv
```
$ pip install opencv-python
```
2. tensorflow
```
$ pip install tensorflow
```
3. imutils
```
$ pip install imutils
```
## Description of files:
### sudoku_grab.py :
This script has the functions which preprocess the input image and extract the sudoku from it.
### cell_extraction.py :
This script has the functions which splits the cells of sudoku and uses the pretrained OCR model to identify the digits written in them and returns the board as a list.
### sudoku_solver.py :
This is main solver where the board (list) is solved using backtracking algorithm.
### display_soln.py :
This script has the funcitons which are used to display the solution on the input image.

## Examples :
1. sudokus/sudoku3.jpg


