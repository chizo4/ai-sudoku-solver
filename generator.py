'''
SUDOKU SOLVER PROJECT: Sudoku board generator.

Date created:
    03/2022

Author:
    Filip J. Cierkosz
'''

import numpy as np

class SudokuGenerator:
    def __init__(self):
        '''
        Constructor for the board generator. Initialized with 9x9 array 
        filled with 0's. numsToAppend denotes the amount of numbers visible 
        on the generated grid; varies with values of 7-12.

            Parameters:
                self
        '''
        self.GRID_SIZE = 9
        self.numsToAppend = np.random.randint(7,13)
        self.genBoard = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int)

    def validate(self, coords, num):
        '''
        Validates a new number to be added to the grid.

            Parameters:
                coords (tuple) : Tuple containing x and y coordinates.
                num (int) : New integer to be inserted.
                self
        '''
        row = coords[0]
        col = coords[1]

        # Column validation.
        for r in range(9):
            if (self.genBoard[r][col]==num):
                return False

        # Row validation.
        for c in range(9):
            if (self.genBoard[row][c]==num):
                return False

        # Section validation.
        secRow = row//3
        secCol = col//3

        for r in range(3):
            for c in range(3):
                if (self.genBoard[secRow*3+r][secCol*3+c]==num):
                    return False

        # If none of the conditions were fulfilled, validate the value.
        return True

    def runGenerator(self):
        '''
        Generates a sudoku board, also calling validation functions.

            Parameters:
                self
        '''
        for n in range(self.numsToAppend):
            # Generate random integer 1-9 and coordinates for the grid.
            num = np.random.randint(1, 10)
            coords = (np.random.randint(9), np.random.randint(9))
            
            while (self.genBoard[coords[0]][coords[1]]!=0 or 
                    not self.validate(coords, num)):
                coords = (np.random.randint(9), np.random.randint(9))
                num = np.random.randint(1, 10)

            # Append new random value in randomly selected coordinates.
            self.genBoard[coords[0]][coords[1]] = num
