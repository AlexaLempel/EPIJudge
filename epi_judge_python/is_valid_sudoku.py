from typing import List
import collections
import math

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    region_size = int(math.sqrt(len(partial_assignment)))
    val_counts = collections.Counter([
                tup for i, row in enumerate(partial_assignment)
                for j, val in enumerate(row) if val > 0
                for tup in ((i, str(val)), (str(val), j), (i // region_size, j // region_size, str(val)))
            ])
    return max(val_counts.values(), default=0) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
