from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    n = len(square_matrix)
    if n == 1:
        return [square_matrix[0][0]]
    result = []
    it = 0
    while len(result) < n**2 - 1:
        result += [square_matrix[it][j] 
                   for j in range(it, n - it - 1)]
        result += [square_matrix[i][n - 1 - it] 
                   for i in range(it, n - it - 1)]
        result += [square_matrix[n - 1 - it][j] 
                   for j in reversed(range(it + 1, n - it))]
        result += [square_matrix[i][it] 
                   for i in reversed(range(it + 1, n - it))]
        it += 1

    if n % 2:
        result.append(square_matrix[n//2][n//2])

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
