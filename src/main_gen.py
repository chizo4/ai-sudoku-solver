'''
main.py

Main program for running grid generator and sudoku solver.

Author: Filip J. Cierkosz (2022)
'''


from tools.grid_generator import GridGenerator
from tools.sudoku_solver import SudokuSolver
import numpy as np


def main():
    '''
    Main method to run the sudoku generator and solver.
    '''
    # Generate sudoku grid.
    gen = GridGenerator()
    gen.run_generator()
    # Instantiate SudokuSolver object with the generated grid.
    solver = SudokuSolver(gen.gen_grid)
    print('~~~~~~ Unsolved Sudoku ~~~~~~')
    print(solver)
    # Solve the grid and measure the runtime.
    solver.set_timer()
    solver.run_solver()
    print('~~~~~~ Solved Sudoku ~~~~~~')
    print(solver)
    runtime = solver.stop_timer()
    print(f'\nTime of execution: {runtime:.4f} sec.\n')


# Run the main program.
if __name__=='__main__':
    main()
