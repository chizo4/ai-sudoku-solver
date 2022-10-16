'''
src/solver/solver.py

Sudoku solver implemented using the backtracking algorithm.

Author: Filip J. Cierkosz (2022)
'''


from time import time


class SudokuSolver:
    '''
    -----------
    Class to solve a sudoku grid using backtracking.
    -----------
    '''

    def __init__(self, grid):
        '''
        Constructor initialized with the sudoku grid extracted from an image/generator.

            Parameters:
                self
                bd (np.array) : input sudoku grid (size 9x9).
        '''
        self.grid = grid
        self.start = 0
        self.stop = 0

    def find_empty_spot(self):
        '''
        Finds the first available empty spot in the grid.

            Parameters:
                self

            Returns:
                (c, r) : tuple of available coordinates.
        '''
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c] == 0:
                    return (c, r)
        return False

    def check_if_valid(self, coords, new_num):
        '''
        Validates a new number to be inserted into the grid.

            Parameters:
                self
                coords (tuple) : grid coordinates for a new value.
                newNum (int) : New value to be inserted.

            Returns:
                boolean
        '''
        x = coords[0]
        y = coords[1]

        # Column validation: if a new number already exists in a column and 
        # it is in a different position than inserted, then it is not valid.
        for c in range(len(self.grid)):
            if (self.grid[c][x] == new_num) and (y != c):
                return False

        # Row validation: if a new number already exists in a row and it 
        # is in a different position than inserted, then it is not valid.
        for r in range(len(self.grid[0])):
            if (self.grid[y][r] == new_num) and (x != r):
                return False

        # Section validation (i.e. 3x3 square).
        x_sec = x // 3
        y_sec = y // 3

        for r in range(y_sec * 3, y_sec * 3 + 3):
            for c in range(x_sec * 3, x_sec * 3 + 3):
                # If a number exists in the section and is in a different 
                # position than inserted, then it is not valid.
                if (self.grid[r][c] == new_num) and (c != x) and (r != y):
                    return False
        return True

    def run_solver(self):
        '''
        Solves a sudoku grid using backtracking algorithm.

            Parameters:
                self

            Returns:
                boolean
        '''
        empty_spot = self.find_empty_spot()

        # If there are no more empty spots to be found, it means that 
        # the grid has been solved.
        if not empty_spot:
            return True
        else:
            coords = empty_spot
            x = coords[0]
            y = coords[1]

        for n in range(1,10):
            if self.check_if_valid(coords, n):
                self.grid[y][x] = n

                # Call the function recursively to furthermore solve sudoku.
                if self.run_solver():
                    return True

                # If something went incorrect, backtrack to the last edited 
                # element and reset it to 0.
                self.grid[y][x] = 0

        return False

    def set_timer(self):
        '''
        Sets the timer to mesaure runtime.

            Parameters:
                self
        '''
        self.start = time()
        return self.start

    def stop_timer(self):
        '''
        Stops the timer and displays the runtime.

            Parameters:
                self
        '''
        self.stop = time()
        return self.stop - self.start

    def __str__(self):
        '''
        String representation of the sudoku grid.

            Parameters:
                self

            Returns:
                outputStr (str) : String representation for a sudoku grid.
        '''
        output_str = '-------------------------'+'\n'

        for i in range(len(self.grid)):
            if i != 0 and (i % 3) == 0:
                output_str += '|-------+-------+-------|'+'\n'

            for j in range(len(self.grid[0])):
                if j != 0 and (j % 3) == 0:
                    output_str += '| '

                if j == 0:
                    output_str += f'| {self.grid[i][j]} '
                elif j == 8:
                    output_str += f'{self.grid[i][j]} |'+'\n'
                else:
                    output_str += f'{self.grid[i][j]} '

        output_str += '-------------------------'
        return output_str
