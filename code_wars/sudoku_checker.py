__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '01-13-2020'

import numpy as np

"""
https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/train/python
"""


def done_or_not(board):
    result = 'Try again!'
    _nd_board = np.asarray(board)
    (row, col) = _nd_board.shape
    print(f"{row}, {col}")
    is_valid = lambda a: np.unique(a).shape == a.shape
    for i in range(row):
        if not is_valid(_nd_board[i, :]):
            return result
        if not is_valid(_nd_board[:, i]):
            return result

    block_size = int(row ** .5)

    for i in range(row):
        block_row, block_col = divmod(i, block_size)
        block = _nd_board[block_row * block_size:(block_row + 1) * block_size,
                block_col * block_size:(block_col + 1) * block_size]
        if not is_valid(block.reshape(row)):
            return result
    result = "Finished!"
    return result


if __name__ == "__main__":
    m_board = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
               [4, 9, 8, 2, 6, 1, 3, 7, 5],
               [7, 5, 6, 3, 8, 4, 2, 1, 9],
               [6, 4, 3, 1, 5, 8, 7, 9, 2],
               [5, 2, 1, 7, 9, 3, 8, 4, 6],
               [9, 8, 7, 4, 2, 6, 5, 3, 1],
               [2, 1, 4, 9, 3, 5, 6, 8, 7],
               [3, 6, 5, 8, 1, 7, 9, 2, 4],
               [8, 7, 9, 6, 4, 2, 1, 5, 3]]
    print(done_or_not(m_board))
