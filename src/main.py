'''
main.py

Main program for running generator and solver.

Author: Filip J. Cierkosz (2022)
'''


from generator import SudokuGenerator
from solver import SudokuSolver
import numpy as np


def main():
    '''
    Main method to run the sudoku generator and solver.
    '''
    # Specify random number of trails, in range 1-20.
    trials = np.random.randint(1, 21)
    runtimes = np.empty(trials)

    # Perform the trails.
    for i in range(trials):
        gen = SudokuGenerator()
        gen.run_generator()

        # Instantiate a SudokuSolver object using the generated board.
        print(f'Board #{i+1} before being solved:')
        solved = SudokuSolver(gen.get_gen_board())
        print(solved)

        # Solve the board and measure the runtime.
        solved.set_timer()
        solved.run_solver()
        print(f'Board #{i+1} after being solved:')
        print(solved)
        time_one_trial = solved.stop_timer()
        print(f'Time of execution: {time_one_trial:.4f} sec.\n\n')

        runtimes[i] = time_one_trial

    # Get the average runtime for solving one sudoku.
    avg_time = np.average(runtimes)
    print('-----------------------------------------------------------------------------')
    print(f'Average runtime for solving one sudoku after {trials} trials: {avg_time:.4f} sec.')
    print('-----------------------------------------------------------------------------')

# Run the main program.
if (__name__=='__main__'):
    main()
