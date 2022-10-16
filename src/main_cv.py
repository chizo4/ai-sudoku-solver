'''
src/main_cv.py

Main program for running computer vision implementation sample.

Author: Filip J. Cierkosz (2022)
'''


from tools.sudoku_solver import SudokuSolver
from tools.image_processing import *
import numpy as np


def main(img_path):
    '''
    Main for the computer vision implementation.

        Parameters:
            img_path : path of the randomly selected image.
    '''
    # Image processing tasks to finally extract digits from sudoku.
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    cv2.imshow('Unsolved Sudoku', img)
    img = resize_img(img)
    contours = preprocess_img(img)
    img = transform_plane(contours, img)
    unsolved_grid = classify_digits(img)
    unsolved_grid = np.array(unsolved_grid).reshape((9, 9))
    # Find solution to the sudoku.
    unsolved = unsolved_grid.copy()
    solver = SudokuSolver(unsolved)
    solver.run_solver()
    solved_grid = solver.grid
    print(solved_grid)
    # Display digits and present the results in the final image.
    final_img = display_digits(img, unsolved_grid, solved_grid)
    cv2.imshow('Solved Sudoku', final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Run the main program.
if __name__=='__main__':
    # Select sample image.
    rand_img_num = np.random.randint(5)
    img_path = f'assets/{rand_img_num}.png'
    main(img_path)
