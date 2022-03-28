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
        Constructor for the board generator. 
        Initialized with 9x9 array filled with 0's.
        numsToAppend denotes the amount of correct numbers visible on the grid.

            Parameters:
                self
        '''
        self.GRID_SIZE = 9
        self.numsToAppend = np.random.randint(7,13)
        self.genBoard = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int)

    def validate(self, mesh, r, c, n):
        '''
        X

            Parameters:
                self
        '''
        # Check column.
        for y in range(9):
            if mesh[r][y]==n:
                return False

        # Check row.
        for x in range(9):
            if mesh[x][c] == n:
                return False

        rowSection = r//3
        colSection = c//3

        for x in range(3):
            for y in range(3):
                # Section validation.
                if mesh[rowSection*3+x][colSection*3+y]==n:
                    return False

        return True

    def runGenerator(self):
        '''
        X

            Parameters:
                self
        '''
        # Generate random values for the grid.
        for i in range(self.numsToAppend):
            row = np.random.randint(9)
            col = np.random.randint(9)
            num = np.random.randint(1, 10)

            while not self.validate(self.genBoard, row, col, num) or self.genBoard[row][col]!=0:
                row = np.random.randint(9)
                col = np.random.randint(9)
                num = np.random.randint(1, 10)

            self.genBoard[row][col] = num

        



# testing --->

test = SudokuGenerator()
#test.runGenerator()

test.runGenerator()

print(test.genBoard)

#print(test.runGenerator())


# till here <---







# TEMPORARILY
#appendedNums = 8
#GRID_SIZE = 9
#grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Validation.
def validate(mesh, r, c, n):
    #valid = True

    # Check row and column.
    for x in range(9):
        if mesh[x][c] == n:
            #valid = False
            #break
            return False

    for y in range(9):
        if mesh[r][y] == n:
            return False
            #valid = False
            #break

    rowSection = r//3
    colSection = c//3

    for x in range(3):
        for y in range(3):
            # Section validation.
            if mesh[rowSection*3+x][colSection*3+y]==n:
                #valid = False
                #break
                return False

    #return valid
    return True

# Generate random values for the grid.
'''for i in range(appendedNums):
    row = np.random.randint(9)
    col = np.random.randint(9)
    num = np.random.randint(1, 10)

    while not validate(grid, row, col, num) or grid[row][col]!=0:
        row = np.random.randint(9)
        col = np.random.randint(9)
        num = np.random.randint(1, 10)

    grid[row][col] = num'''



'''for y in range (9):
    for x in range(9):
        print(grid[y][x])'''


#print(grid)






