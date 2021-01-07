import numpy as np

# Sudoku solver project
# for my Design and Analysis of Algorithms Class taught by Prof. HajAhmadi
# solution by Parsa KamaliPour.


def find_next_empty(puzzle):
    # this function finds next empty spot on the puzzle looking through rows and columns, empty spots are filled with -1
    # returns tuple (row, col) of our empty spot, if no empty spaces were spotted returns (none, none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):  # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no empty spaces were spotted return null


def is_valid(puzzle, guess, row, col):
    # figures out if our guess at this (row, col) is valid using sudoku rules.
    # returns true when our guess is valid option, else false

    # for a guess to be valid, we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_vals = puzzle[row]   # copy this specific row in a new list called row_vals
    if guess in row_vals:
        return False  # if our guess was spotted in it's row return false because we have violated sudoku rules

    # now the column
    col_vals = [puzzle[i][col] for i in range(9)]  # copy this specific entire column in a new list called col_vals
    if guess in col_vals:
        return False  # if our guess was spotted in it's column return false because we have violated sudoku rules

    # and then the square
    row_start = (row // 3) * 3    # we're finding starting point of our guess' square in rows (options: 0, 3, 6)
    col_start = (col // 3) * 3    # we're finding starting point of our guess' square in columns (options: 0, 3, 6)

    for r in range(row_start, row_start + 3):        # move from square's starting point up to last point in that square
        for c in range(col_start, col_start + 3):    # move from square's starting point up to last point in that square
            if puzzle[r][c] == guess:
                # if our guess was spotted in it's square return false because we have violated sudoku rules
                return False

    return True  # our guess is valid option


def solve_sudoku(puzzle):
    # we're solving this puzzle using Backtracking algorithm
    # our puzzle is a list of lists holding 9 Rows (which are lists) and each Row is a list of 9 columns
    # if this function returns true it indicates that this puzzle is solved, else it's unsolvable.

    # step 1: find a empty space on the puzzle to mutate it
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's no empty spaces left in our puzzle which means we're done return True (puzzle is solved)
    if row is None:  # this is true if our find_next_empty function returns (None, None)
        return True

    # step 2: if there is an empty place on our puzzle, guess a number between 1 .. 9
    for guess in range(1, 10):  # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if our guess is valid using sudoku rules (row, col, block is valid)
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if our guess is a valid answer put it on that spot in our puzzle
            puzzle[row][col] = guess
            # step 4: then we call our solve_sudoku function recursively with our updated puzzle
            if solve_sudoku(puzzle):
                return True        # once our puzzle is fully solved return True

        # step 5: if our guess isn't valid or puzzle couldn't be solved, Backtrack and revert spot on the puzzle to -1
        puzzle[row][col] = -1

    # step 6: if none of our guesses worked, it indicates that this puzzle can't be solved
    return False


if __name__ == '__main__':

    sudoku = [
        [5, 3, -1,     -1, 7, -1,     -1, -1, -1],
        [6, -1, -1,      1, 9, 5,     -1, -1, -1],
        [-1, 9, 8,    -1, -1, -1,      -1, 6, -1],

        [8, -1, -1,     -1, 6, -1,     -1, -1, 3],
        [4, -1, -1,      8, -1, 3,     -1, -1, 1],
        [7, -1, -1,     -1, 2, -1,     -1, -1, 6],

        [-1, 6, -1,     -1, -1, -1,      2, 8, -1],
        [-1, -1, -1,       4, 1, 9,     -1, -1, 5],
        [-1, -1, -1,      -1, 8, -1,      -1, 7, 9]
    ]

    print(solve_sudoku(sudoku))  # solve our puzzle then print the result which if it was successful or not
    print(np.matrix(sudoku))     # print our solved puzzle as a matrix using NumPy library
