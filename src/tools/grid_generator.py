'''
src/tools/grid_generator.py

Generator for sudoku grids. 

Author: Filip J. Cierkosz (2022)
'''


import numpy as np


class GridGenerator:
    '''
    -----------
    Class to generate a sudoku board.
    -----------
    '''

    def __init__(self):
        '''
        Constructor for the board generator. Initialized with 9x9 array 
        filled with 0's. numsToAppend denotes the amount of numbers visible 
        on the generated grid; varies with values of 7-9.

            Parameters:
                self
        '''
        self.GRID_SIZE = 9
        self.nums_to_append = np.random.randint(7,10)
        self.gen_grid = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int)

    def validate(self, coords, num):
        '''
        Validates a new number to be added to the grid.

            Parameters:
                coords (tuple) : Tuple containing x and y coordinates.
                num (int) : New integer to be inserted.
                self

            Returns:
                boolean
        '''
        row = coords[0]
        col = coords[1]

        # Column validation.
        for r in range(9):
            if self.gen_grid[r][col] == num:
                return False

        # Row validation.
        for c in range(9):
            if self.gen_grid[row][c] == num:
                return False

        # Section validation.
        sec_row = row // 3
        sec_col = col // 3

        for r in range(3):
            for c in range(3):
                if self.gen_grid[sec_row * 3 + r][sec_col * 3 + c] == num:
                    return False

        # If none of the conditions were fulfilled, validate the value.
        return True

    def run_generator(self):
        '''
        Generates a sudoku board, also calling validation functions.

            Parameters:
                self
        '''
        for _ in range(self.nums_to_append):
            num = np.random.randint(1, 10)
            coords = (np.random.randint(9), np.random.randint(9))
            
            while self.gen_grid[coords[0]][coords[1]]!=0 or not self.validate(coords, num):
                coords = (np.random.randint(9), np.random.randint(9))
                num = np.random.randint(1, 10)

            # Append new random value in randomly selected coordinates.
            self.gen_grid[coords[0]][coords[1]] = num
