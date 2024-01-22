from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    offset = 0
    n = len(square_matrix)
    while offset < n//2:
        for j in range(offset, n - 1 - offset):
            i1, j1 = offset, j
            i2, j2 = j, n - 1 - offset
            i3, j3 = n - 1 - offset, n - 1 - j
            i4, j4 = n - 1 - j, offset

            temp = square_matrix[i4][j4]
            square_matrix[i4][j4] = square_matrix[i3][j3]
            square_matrix[i3][j3] = square_matrix[i2][j2]
            square_matrix[i2][j2] = square_matrix[i1][j1]
            square_matrix[i1][j1] = temp 

        offset += 1
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
