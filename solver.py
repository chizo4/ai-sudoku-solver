'''
SUDOKU SOLVER PROJECT: AI sudoku solver (implementing backtracking algorithm).

Date created (initial file of the project):
    12/2021

Date modified:
    03/2022

Author:
    Filip J. Cierkosz
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
        # Set the board.
        self.board = bd
        # Variables used for timer.
        self.start = 0
        self.stop = 0

    def findEmptySpot(self):
        '''
        Finds the first available empty spot in the board.

            Parameters:
                self

            Returns:
                boolean
        '''
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                # Find the first element that is equal to 0 (denoting an empty spot).
                if (self.board[r][c]==0):
                    # Return the coordinates of the found spot.
                    return (c, r)

        # If there are no available spots, return False.
        return False

    def checkIfValid(self, coords, newNum):
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

        # Column validation.
        for c in range(len(self.board)):
            # If a new number already exists in a column and it is in a different
            # position than inserted, then it is not valid.
            if (self.board[c][x]==newNum and y!=c):
                return False

        # Row validation. 
        for r in range(len(self.board[0])):
            # If a new number already exists in a row and it is in a different 
            # position than inserted, then it is not valid.
            if (self.board[y][r]==newNum and x!=r):
                return False

        # Section validation (i.e. 3x3 square).
        xSec = x//3
        ySec = y//3

        for r in range(ySec*3, ySec*3+3):
            for c in range(xSec*3, xSec*3+3):
                # If a number exists in the section and is in a different 
                # position than inserted, then it is not valid.
                if (self.board[r][c]==newNum and c!=x and r!=y):
                    return False

        # If no conditions met, the number is valid and can be inserted.
        return True

    def runSolver(self):
        '''
        Solves a sudoku board using backtracking algorithm.

            Parameters:
                self

            Returns:
                boolean
        '''
        emptySpot = self.findEmptySpot()

        # If there are no more empty spots to be found, it means that 
        # the board has been solved.
        if (not emptySpot):
            return True
        # Otherwise, run the solver.
        else:
            coords = emptySpot
            x = coords[0]
            y = coords[1]

        # Iterate through all the possible numbers for the board, i.e. 1-9.
        for n in range(1,10):
            # If a number passes the validity check, append it in the board.
            if (self.checkIfValid(coords, n)):
                self.board[y][x] = n

                # Call the function recursively to furthermore solve sudoku.
                if self.runSolver():
                    return True

                # If something went incorrect, backtrack to the last edited 
                # element and reset it to 0.
                self.board[y][x] = 0

        # If none of the numbers are valid return False.
        return False

    def setTimer(self):
        '''
        Sets the timer to mesaure runtime.

            Parameters:
                self
        '''
        self.start = time()
        return self.start

    def stopTimer(self):
        '''
        Stops the timer and displays the runtime.

            Parameters:
                self
        '''
        self.stop = time()
        # Calculate the delta of the runtime.
        print(f'Time of execution: {self.stop-self.start:.4f} sec.')

    def __str__(self):
        '''
        String representation of the sudoku board.

            Parameters:
                self

            Returns:
                outputStr (str) : String representation for a sudoku board.
        '''
        outputStr = '-------------------------'+'\n'

        # Iterate through the 2D array, display elements separating subareas of the board.
        for i in range(len(self.board)):
            if (i!=0 and i%3==0):
                outputStr += '|-------+-------+-------|'+'\n'

            for j in range(len(self.board[0])):
                # Display the horizontal lines separating smaller squares of board.
                if (j!=0 and j%3==0):
                    outputStr += '| '

                # Display the values of the board along with outer borders.
                if (j==0):
                    outputStr += f'| {self.board[i][j]} '
                elif (j==8):
                    outputStr += f'{self.board[i][j]} |'+'\n'
                else:
                    outputStr += f'{self.board[i][j]} '

        outputStr += '-------------------------'

        return outputStr
