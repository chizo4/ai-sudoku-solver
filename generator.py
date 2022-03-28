'''
SUDOKU SOLVER PROJECT: Sudoku board generator.

Date created:
    03/2022

Author:
    Filip J. Cierkosz
'''

import numpy as np

#class SudokuGenerator:
    #def __init__(self):
        #'''
        #Constructor for the board generator. Initialized with 9x9 array filled with 0's.

            #Parameters:
                #self
        #'''
        #self.generatedBoard = 0








# TEMPORARILY
appendedNums = 8
GRID_SIZE = 9
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Validation.
def validate(mesh, r, c, n):
    valid = True

    # Check row and column.
    for x in range(9):
        if mesh[x][c] == n:
            valid = False
            break

    for y in range(9):
        if mesh[r][y] == n:
            valid = False
            break

    rowSection = r//3
    colSection = c//3

    for x in range(3):
        for y in range(3):
            # Section validation.
            if mesh[rowSection*3+x][colSection*3+y]==n:
                valid = False
                break

    return valid

# Generate random values for the grid.
for i in range(appendedNums):
    row = np.random.randint(9)
    col = np.random.randint(9)
    num = np.random.randint(1, 10)

    while not validate(grid, row, col, num) or grid[row][col]!=0:
        row = np.random.randint(9)
        col = np.random.randint(9)
        num = np.random.randint(1, 10)

    grid[row][col] = num

counter = 0

'''for y in range (9):
    for x in range(9):
        print(grid[y][x])'''


print(grid)




