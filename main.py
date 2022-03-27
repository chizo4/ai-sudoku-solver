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

# Function 4: Display the sudoku board. The function can be used if 
# the purpose of the program is only to solve the board (and so there
# would be no GUI).
def displayBoard(board):
    # Display the top border.
    print('-------------------------')

    # Iterate through the 2D array, display elements and separate the 
    # subareas of the board.
    for i in range(len(board)):
        # Display the vertical lines separating 3x3 squares of the board.
        if (i!=0 and i%3==0):
            print('|-------+-------+-------|')

        for j in range(len(board[0])):
            # Display the horizontal lines separating smaller squares of board.
            if (j!=0 and j%3==0):
                print('| ', end='')

            # Display the values of the board along with outer borders.
            if (j==0):
                print(f'| {board[i][j]} ', end='')
            elif (j==8):
                print(f'{board[i][j]} |')
            else:
                print(f'{board[i][j]} ', end='')

    # Display the bottom border.
    print('-------------------------')

# Function 5: Set the timer.
def setTimer():
    start = time()
    return start

# Function 6: Stop the timer and return the time of execution.
def stopTimer(start):
    stop = time()
    print(f'Time of execution: {stop-start}\n')

# ----------TEST HARNESS----------
# Array containing board samples to solve.
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
    [[5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]],

    # Board 5.
    [[9,0,0,0,8,0,0,0,1],
    [0,0,0,4,0,6,0,0,0],
    [0,0,5,0,7,0,3,0,0],
    [0,6,0,0,0,0,0,4,0],
    [4,0,1,0,6,0,5,0,8],
    [0,9,0,0,0,0,0,2,0],
    [0,0,7,0,3,0,2,0,0],
    [0,0,0,7,0,5,0,0,0],
    [1,0,0,0,4,0,0,0,7]]
]

# Iterate through the samples and solve each board.
for board in sudokuBoardsArr:
    # Set the timer.
    start = setTimer()

    # Running number.
    num = sudokuBoardsArr.index(board)+1

    # Display the board before invoking functions.
    print(f'The board no. #{num} before being solved:')
    displayBoard(board)
    print()

    # Display the board after being solved.
    print(f'The board no. #{num} after being solved:')
    solveSudoku(board)
    displayBoard(board)

    # Display the time of execution for a single board.
    stopTimer(start)
