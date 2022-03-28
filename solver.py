'''
SUDOKU SOLVER PROJECT: AI bot implementing the backtracking 
                       algotrithm to solve sudoku.

Date created:
    12/2021

Date modified:
    03/2022

Author:
    Filip J. Cierkosz
'''

from time import time

class Solver:
    '''
    -----------
    Class to solve a sudoku board.
    -----------
    '''
    def __init__(self, bd):
        '''
        Constructor initialized with a generated unsolved sudoku board.

            Parameters:
                self
                bd (array) : Generated sudoku board (with size 9x9).
        '''
        self.board = bd

    def findEmptySpot(self):
        # Iterate through the rows and columns of the board.
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                # Find the first element that is equal to 0. It denotes an empty spot.
                if (self.board[row][col]==0):
                    # Return the coordinates of the spot.
                    return [col, row]

        # If there are no more empty spots, return False.
        return False


    def checkIfValid(self, coords, newNum):
        # Define coordinates.
        x = coords[0]
        y = coords[1]

        # Check column.
        # Iterate through the elements of a column.
        for i in range(len(board)):
            # If a new number already exists in a column and it is in a different
            # position than inserted, it is not valid and cannot be inserted.
            if (self.board[i][x]==newNum and y!=i):
                return False

        # Check row. 
        # Iterate through elements of a row.
        for i in range(len(self.board[0])):
            # If a new number already exists in a row and it is in a different 
            # position than inserted, it is not valid and cannot be inserted.
            if (self.board[y][i]==newNum and x!=i):
                return False

        # Check 3x3 square.
        # Determine the square by its coordinates.
        xSquare = x//3
        ySquare = y//3

        # Iterate through the elements of a 3x3 square.
        for row in range(ySquare*3, ySquare*3+3):
            for col in range(xSquare*3, xSquare*3+3):
                # If a number exists in the 3x3 square of the board and is 
                # in a different position than inserted, it is not valid
                # and cannot be inserted.
                if (self.board[row][col]==newNum and col!=x and row!=y):
                    return False

        # If none of the conditions above were met, the number is valid and 
        # so can be inserted in the board.
        return True

    def solve(self):
        # Find an empty spot in the board.
        emptySpot = self.findEmptySpot(self.board)

        # If there are no more empty spots to be found, it means that 
        # the board has been solved.
        if (not emptySpot):
            return True
        else:
            coords = emptySpot
            x = coords[0]
            y = coords[1]

        # Iterate through all the possible numbers for the board, i.e. 1-9.
        for n in range(1,10):
            # If a number passes the validity check, append it in the board.
            if (self.checkIfValid(self.board, coords, n)):
                self.board[y][x] = n

                # Call the function recursively to solve the sudoku furthermore.
                if self.solveSudoku(self.board):
                    return True

                # If something is not correct, backtrack to the last edited 
                # element and reset it to 0.
                self.board[y][x] = 0

        # If none of the numbers are valid return False.
        return False

    # Function 5: Set the timer.
    def setTimer():
        start = time()
        return start

    # Function 6: Stop the timer and return the time of execution.
    def stopTimer(start):
        stop = time()
        print(f'Time of execution: {stop-start}\n')
