# GUI for SUDOKU SOLVER.
# Written by: Filip J. Cierkosz
# Date: 12/2021

from main import checkIfValid, solveSudoku
from time import time
import random
import pygame
pygame.font.init()

# ----------CLASS FOR A SUDOKU BOARD----------
class Board:
    # Array containing samples of boards to solve.
    sudokuBoardsArr = [
        # Board 1.
        [
            [0,0,4,0,0,0,3,0,0],
            [2,0,0,7,0,9,0,0,8],
            [0,6,0,5,0,4,0,7,0],
            [0,0,5,0,7,0,2,0,0],
            [4,0,0,3,0,5,0,0,9],
            [0,0,7,0,9,0,5,0,0],
            [0,4,0,9,0,2,0,5,0],
            [8,0,0,6,0,7,0,0,2],
            [0,0,9,0,0,0,1,0,0]
        ],
        
        # Board 2.
        [
            [0,0,5,1,0,9,3,0,0],
            [0,2,0,0,0,0,0,9,0],
            [4,0,9,0,0,0,6,0,5],
            [1,0,0,8,3,6,0,0,7],
            [0,0,0,2,0,1,0,0,0],
            [9,0,0,5,4,7,0,0,1],
            [2,0,3,0,0,0,1,0,9],
            [0,1,0,0,0,0,0,8,0],
            [0,0,8,7,0,5,4,0,0]
        ],
        
        # Board 3.
        [
            [0,5,0,0,3,0,0,8,0],
            [3,0,7,0,0,0,6,0,5],
            [0,9,0,5,0,8,0,7,0],
            [0,0,8,7,0,1,4,0,0],
            [9,0,0,0,0,0,0,0,7],
            [0,0,5,9,0,3,1,0,0],
            [0,1,0,8,0,4,0,2,0],
            [8,0,4,0,0,0,9,0,1],
            [0,6,0,0,1,0,0,4,0]
        ],

        # Board 4.
        [
            [4,6,0,0,8,0,0,5,1],
            [0,0,0,0,6,0,0,0,0],
            [0,0,0,1,0,5,0,0,0],
            [0,0,5,0,4,0,3,0,0],
            [0,7,0,2,0,3,0,4,0],
            [0,3,0,0,5,0,0,1,0],
            [0,0,9,0,0,0,5,0,0],
            [0,1,6,4,3,8,9,2,0],
            [0,8,0,0,0,0,0,3,0]
        ],

        # Board 5.
        [
            [0,1,0,0,0,0,5,6,0],
            [7,0,0,0,4,2,0,0,9],
            [3,0,0,0,0,0,0,0,0],
            [0,9,0,5,2,4,0,0,0],
            [0,2,0,6,0,9,0,1,0],
            [0,0,0,8,1,7,0,3,0],
            [0,0,0,0,0,0,0,0,3],
            [4,0,0,2,5,0,0,0,8],
            [0,6,2,0,0,0,0,5,0]
        ],

        # Board 6.
        [
            [5,0,0,0,1,0,0,0,7],
            [0,8,0,0,2,0,0,5,0],
            [0,4,0,5,0,6,0,2,0],
            [1,9,0,0,0,0,0,4,8],
            [0,0,0,0,7,0,0,0,0],
            [0,0,0,4,8,9,0,0,0],
            [0,2,9,0,0,0,3,1,0],
            [0,0,0,1,0,8,0,0,0],
            [3,0,0,9,5,2,0,0,4]
        ],

        # Board 7.
        [
            [0,0,0,0,0,0,0,9,0],
            [9,0,1,3,0,5,8,0,0],
            [0,5,0,0,0,7,0,3,0],
            [0,4,2,0,9,0,0,8,0],
            [0,0,0,7,5,4,0,0,0],
            [0,9,0,0,1,0,5,6,0],
            [0,1,0,8,0,0,0,5,0],
            [0,0,7,5,0,1,2,0,9],
            [0,6,0,0,0,0,0,0,0]
        ],

        # Board 8.
        [
            [0,0,3,7,0,4,1,0,0],
            [0,4,0,0,0,0,0,8,0],
            [0,0,5,0,0,0,2,0,0],
            [5,0,0,4,0,1,0,0,8],
            [0,3,2,6,0,8,5,9,0],
            [4,0,0,5,0,9,0,0,3],
            [0,0,1,0,0,0,9,0,0],
            [0,2,0,0,0,0,0,5,0],
            [0,0,9,1,0,3,4,0,0]
        ],

        # Board 9.
        [
            [0,1,0,0,0,0,0,2,0],
            [5,0,0,6,0,4,0,0,7],
            [0,0,7,2,0,0,8,0,0],
            [0,8,0,0,9,0,1,6,0],
            [0,0,0,5,0,2,0,0,0],
            [0,3,9,0,1,0,0,5,0],
            [0,0,3,0,0,8,6,0,0],
            [1,0,0,9,0,3,0,0,5],
            [0,6,0,0,0,0,0,9,0]
        ]
    ]

    # Select a random board from the array.
    random.choice(sudokuBoardsArr)

    # Initialize a board.
    def __init__(self, width, height, rows, cols):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.cubes = []
        self.select = None
        self.model = None

    def updateModel():
        pass

    def place():
        pass

    def click():
        pass

    def clear():
        pass

    def select():
        pass

    def sketch():
        pass
    
    def draw():
        pass

    def isFinished():
        pass


# ----------CLASS FOR A CUBE----------
class Cube:
    rows = 9
    cols = 9

    # Initialize a cube.
    def __init__(self, width, height, row, col, num):
        self.select = False
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.tempNum = 0
        self.num = num

    # 
    def draw(self, win):
        pass

    def setNum():
        pass

    def setTemp():
        pass

# ----------FUNCTIONS----------
def redrawWindow():
    pass

def timer():
    return None

def main():
    pass








#main()
#pygame.quit()