'''
SUDOKU SOLVER PROJECT: Main program for running generator and solver.

Date created:
    03/2022

Author:
    Filip J. Cierkosz
'''

from generator import SudokuGenerator
from solver import SudokuSolver
import numpy as np

def main():
    '''
    Main method to run the sudoku generator and solver.
    '''
    # Specify random number of trails, in range 1-20.
    trails = np.random.randint(1, 21)

    # Perform the trails.
    for i in range(trails):
        # Instantiate a SudokuGenerator object.
        gen = SudokuGenerator()
        gen.runGenerator()

        # Instantiate a SudokuSolver object using the generated board.
        print(f'Board #{i+1} before being solved:')
        solved = SudokuSolver(gen.getGenBoard())
        print(solved)
        solved.setTimer()

        # Solve the board and measure the runtime.
        solved.runSolver()
        print(f'Board #{i+1} after being solved:')
        print(solved)
        solved.stopTimer()
        print()

# Run the main program.
if (__name__=='__main__'):
    main()
