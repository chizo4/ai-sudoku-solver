# SUDOKU SOLVER with the implementation of the backtracking algotrithm.
# Written by: Filip J. Cierkosz
# Date: 12/2021

from time import time

# ----------FUNCTIONS----------
# Function 1: Find an empty spot in the board and return its coordinates.
def findEmptySpot(board):
    # Iterate through the rows and columns of the board.
    for row in range(len(board)):
        for col in range(len(board[row])):
            # Find the first element that is equal to 0. It denotes an empty spot.
            if (board[row][col]==0):
                # Return the coordinates of the spot.
                return [col, row]

    # If there are no more empty spots, return False.
    return False

# Function 2: Verify if the number to insert is valid.
def checkIfValid(board, coords, newNum):
    # Define coordinates.
    x = coords[0]
    y = coords[1]

    # Check column.
    # Iterate through the elements of a column.
    for i in range(len(board)):
        # If a new number already exists in a column and it is in a different
        # position than inserted, it is not valid and cannot be inserted.
        if (board[i][x]==newNum and y!=i):
            return False

    # Check row. 
    # Iterate through elements of a row.
    for i in range(len(board[0])):
        # If a new number already exists in a row and it is in a different 
        # position than inserted, it is not valid and cannot be inserted.
        if (board[y][i]==newNum and x!=i):
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
            if (board[row][col]==newNum and col!=x and row!=y):
                return False

    # If none of the conditions above were met, the number is valid and 
    # so can be inserted in the board.
    return True

# Function 3: Solve the board implementing the backtracking algorithm.
def solveSudoku(board):
    # Find an empty spot in the board.
    emptySpot = findEmptySpot(board)

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
        if (checkIfValid(board, coords, n)):
            board[y][x] = n

            # Call the function recursively to solve the sudoku furthermore.
            if solveSudoku(board):
                return True

            # If something is not correct, backtrack to the last edited 
            # element and reset it to 0.
            board[y][x] = 0

    # If none of the numbers are valid return False.
    return False
