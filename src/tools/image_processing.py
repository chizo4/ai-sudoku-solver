'''
src/tools/image_processing.py

Computer vision tools for sudoku image processing.

Author: Filip J. Cierkosz (2022)
'''


import numpy as np
import pytesseract
import cv2


def resize_img(img):
    '''
    Resizes an input image.

        Parameters:
            img : raw image.

        Returns:
            res_img : resized image.
    '''
    res_img = cv2.resize(img, (500, 600))
    return res_img

def preprocess_img(img):
    '''
    Applies image pre-processing filters such as: 
        noise removal, adaptive threshold, detecting all contours, etc.

        Parameters:
            img : resized image.

        Returns:
            contours : detected sudoku contours in the image.
    '''
    # Apply grayscale, adaptive threshold, canny and find contours.
    graysc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rm_noise = cv2.fastNlMeansDenoising(
        graysc, templateWindowSize=6, searchWindowSize=21, h=3
    )
    thresh = cv2.adaptiveThreshold(
        rm_noise, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )
    canny = cv2.Canny(thresh, 120, 150, apertureSize=3)
    contours, _ = cv2.findContours(
        canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    return contours

def transform_plane(contours, img):
    '''
    Extracts the sudoku grid from the image by applying plane transformation.

        Parameters:
            contours : array of detected contours. 
            img : input image after applying filters.

        Returns:
            undist_img : undistorted sudoku image.
    '''
    max_area = 0
    max_cont = contours[0]
    for c in contours:
        approx = cv2.approxPolyDP(
            c, 0.01 * cv2.arcLength(c, True), True
        )
        if len(approx == 4):
            curr_area = cv2.contourArea(c)
            if max_area <= curr_area:
                max_area = curr_area
                max_cont = approx
    # Refine points for the new plane.
    coords = max_cont.ravel()
    size = 250
    pts_curr, pts_new = specify_points(coords, size)
    # Perform plane transformation.
    plane_trans = cv2.getPerspectiveTransform(pts_curr, pts_new)
    undist_img = cv2.warpPerspective(img, plane_trans, (size, size))
    return undist_img

def specify_points(coords, size):
    '''
    Specifies point for the plane transformation.

        Parameters:
            coords : raw contour points.
            size : size.

        Returns:
            pts_curr : current plane point adjustments.
            pts_new : point adjustments for the new plane.
    '''
    # Arrange points.
    pts = np.float32([
        [coords[0], coords[1]],
        [coords[2], coords[3]],
        [coords[4], coords[5]],
        [coords[6], coords[7]]
    ])
    pts_curr = pts.copy()
    sum_pts = sorted([p[0] + p[1] for p in pts])
    for i in range(0, len(sum_pts)):
        for p in pts:
            if p[0] + p[1] == sum_pts[i]:
                try:
                    if i == 0:
                        pts_curr[1] = [p[0], p[1]]
                    elif i == 1:
                        pts_curr[2] = [p[0], p[1]]
                    elif i == 2:
                        pts_curr[0] = [p[0], p[1]]
                    elif i == 3:
                        pts_curr[3] = [p[0], p[1]]
                except:
                    print('Error - failed to refine points.')
    # Set up new points.
    pts_new = np.float32([
        [0, size],
        [0, 0],
        [size ,0],
        [size, size]
    ])
    return pts_curr, pts_new

def classify_digits(img):
    '''
    Classifies digits (with Google Pytesseract) from an unsolved sudoku image.

        Parameters:
            img : image of unsolved sudoku.

        Returns:
            class_digits : list of classified digits.
    '''
    # Resize and apply filters for the image.
    img = cv2.resize(img, (900, 900))
    graysc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(graysc, 140, 255, cv2.THRESH_BINARY)
    # Specify dimensions.
    width = img.shape[0]
    height = img.shape[1]
    w = width // 9
    h = height // 9
    # Classify digit for each cell using Pytesseract engine.
    class_digits = []
    for r in range(0, width, w):
        for c in range(0, height, h):
            cell_img = thresh[r + 10 : r + w - 10, c + 10 : c + h - 10]
            init_digit = pytesseract.image_to_string(
                cell_img, lang='eng', 
                config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789'
            )
            try:
                digit = int(init_digit)
            except:
                digit = 0
            class_digits.append(digit)
    return class_digits

def display_digits(img, uns_grid, sol_grid):
    '''
    Prints missing digits in the original image after solving sudoku.

        Parameters:
            img : image to draw the digits.
            uns_grid : state of unsolved grid (to compare with solved grid).
            sol_grid : state of solved grid (to compare with unsolved grid).

        Returns:
            img : final image of solved sudoku.
    '''
    # Resize image slightly and specify dimensions.
    img = cv2.resize(img, (450, 450))
    width = img.shape[0]
    w = width // 9
    height = img.shape[1]
    h = height // 9
    # Find coords of zeros in the unsolved grid.
    zero_index = np.where(uns_grid == 0)
    zero_coords = list(zip(zero_index[0], zero_index[1]))
    # Draw a digit from solved grid if it was previously a zero.
    for coords in zero_coords:
        r, c = coords
        x = c * w
        y = r * h
        cv2.putText(
            img, str(sol_grid[r][c]), (int((x + w / 3)), int((y + h / 1.5))),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2
        )
    return img
