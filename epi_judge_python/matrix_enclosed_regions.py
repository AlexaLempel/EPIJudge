from collections import deque
from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    m, n = len(board), len(board[0])

    # Add all W squares on the edge to unenclosed set
    unenclosed = {(i,j) for i,j in [(i,j) for k in range(n) for i,j in ((0, k), (m-1, k))] 
                  + [(i,j) for k in range(m) for i,j in ((k, 0), (k, n-1))]
                  if board[i][j] == 'W'}

    to_visit = deque(unenclosed)

    # W squares connected to squares in queue are also unenclosed
    # Find them with BFS
    while to_visit:
        x,y = to_visit.popleft()
        unenclosed.add((x,y))

        for i,j in ((x, y+1), (x, y-1), (x + 1, y), (x-1, y)):
            if (0 <= i < m and 0 <= j < n and board[i][j] == "W"
                and not (i,j) in unenclosed):
                to_visit.append((i,j))

    for i in range(m): 
        for j in range(n):
            if not (i,j) in unenclosed:
                board[i][j] = 'B'
        
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
