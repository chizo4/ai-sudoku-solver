'''
solver.py

AI sudoku solver (implemented with backtracking algorithm).

Author: Filip J. Cierkosz (2022)
'''


from time import time


class SudokuSolver:
    '''
    -----------
    Class to solve a sudoku board.
    -----------
    '''

    def __init__(self, bd):
        '''
        Constructor initialized with a generated unsolved sudoku board.

            Parameters:
                bd (array) : Generated sudoku board (with size 9x9).
                self
        '''
        self.board = bd
        self.start = 0
        self.stop = 0

    def find_empty_spot(self):
        '''
        Finds the first available empty spot in the board.

            Parameters:
                self

            Returns:
                boolean
        '''
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    return (c, r)

        return False

    def check_if_valid(self, coords, new_num):
        '''
        Validates a new number to be inserted into the board.

            Parameters:
                coords (tuple) : Board coordinated for a new value.
                newNum (int) : New value to be inserted.
                self

            Returns:
                boolean
        '''
        x = coords[0]
        y = coords[1]

        # Column validation: if a new number already exists in a column and 
        # it is in a different position than inserted, then it is not valid.
        for c in range(len(self.board)):
            if self.board[c][x] == new_num and y != c:
                return False

        # Row validation: if a new number already exists in a row and it 
        # is in a different position than inserted, then it is not valid.
        for r in range(len(self.board[0])):
            if self.board[y][r] == new_num and x != r:
                return False

        # Section validation (i.e. 3x3 square).
        x_sec = x // 3
        y_sec = y // 3

        for r in range(y_sec * 3, y_sec * 3 + 3):
            for c in range(x_sec * 3, x_sec * 3 + 3):
                # If a number exists in the section and is in a different 
                # position than inserted, then it is not valid.
                if self.board[r][c] == new_num and c != x and r != y:
                    return False

        return True

    def run_solver(self):
        '''
        Solves a sudoku board using backtracking algorithm.

            Parameters:
                self

            Returns:
                boolean
        '''
        empty_spot = self.find_empty_spot()

        # If there are no more empty spots to be found, it means that 
        # the board has been solved.
        if not empty_spot:
            return True
        else:
            coords = empty_spot
            x = coords[0]
            y = coords[1]

        for n in range(1,10):
            # If a number passes the validity check, append it in the board.
            if self.check_if_valid(coords, n):
                self.board[y][x] = n

                # Call the function recursively to furthermore solve sudoku.
                if self.run_solver():
                    return True

                # If something went incorrect, backtrack to the last edited 
                # element and reset it to 0.
                self.board[y][x] = 0

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
        String representation of the sudoku board.

            Parameters:
                self

            Returns:
                outputStr (str) : String representation for a sudoku board.
        '''
        output_str = '-------------------------'+'\n'

        for i in range(len(self.board)):
            if i != 0 and (i % 3) == 0:
                output_str += '|-------+-------+-------|'+'\n'

            for j in range(len(self.board[0])):
                if j != 0 and (j % 3) == 0:
                    output_str += '| '

                if j == 0:
                    output_str += f'| {self.board[i][j]} '
                elif j == 8:
                    output_str += f'{self.board[i][j]} |'+'\n'
                else:
                    output_str += f'{self.board[i][j]} '

        output_str += '-------------------------'

        return output_str
