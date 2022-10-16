'''
main.py

Main program for running generator and solver.

Author: Filip J. Cierkosz (2022)
'''


from tools.grid_generator import GridGenerator
from tools.image_processing import *
from tools.sudoku_solver import SudokuSolver
import numpy as np


# def main():
#     '''
#     Main method to run the sudoku generator and solver.
#     '''
#     # Specify random number of trails, in range 1-20.
#     trials = np.random.randint(1, 21)
#     runtimes = np.empty(trials)

#     # Perform the trails.
#     for i in range(trials):
#         gen = SudokuGenerator()
#         gen.run_generator()

#         # Instantiate a SudokuSolver object using the generated board.
#         print(f'Board #{i + 1} before being solved:')
        # solved = SudokuSolver(gen.get_gen_board())
        # print(solved)

        # # Solve the board and measure the runtime.
        # solved.set_timer()
        # solved.run_solver()
        # print(f'Board #{i + 1} after being solved:')
        # print(solved)
#         time_one_trial = solved.stop_timer()
#         print(f'Time of execution: {time_one_trial:.4f} sec.\n')

#         runtimes[i] = time_one_trial

#     # Get the average runtime for solving one sudoku.
#     avg_time = np.average(runtimes)
#     print('-----------------------------------------------------------------------------')
#     print(f'Average runtime for solving one sudoku after {trials} trials: {avg_time:.4f} sec.')
#     print('-----------------------------------------------------------------------------')


def main():
    '''
    Main runner.
    '''
    # select sample image
    img_path = 'assets/2.png'
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    # resize image
    img = resize_img(img)

    # preprocess
    contours = preprocess_img(img)

    # transform image
    img = transform_plane(contours, img)

    unsolved_grid = classify_digits(img) # reading sudoku table

    # solved_grid = np.array(unsolved_grid).reshape((9, 9))#.tolist()
    unsolved_grid = np.array(unsolved_grid).reshape((9, 9))#.tolist()

    # solving board....
    unsolved = unsolved_grid.copy()
    solver = SudokuSolver(unsolved)
    solver.run_solver()
    solved_grid = solver.grid

    # show final image
    final_img = display_digits(img, unsolved_grid, solved_grid)
    cv2.imshow('Solved Sudoku', final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Run the main program.
if __name__=='__main__':
    main()