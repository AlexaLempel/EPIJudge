from collections import deque
from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    to_visit = deque([(x,y)])
    color = image[x][y]

    while to_visit:
        # Get next pixel from queue
        x,y = to_visit.popleft()

        # Get adjacent pixel coords and add to queue
        # if in bounds, is the target color, and not yet visited
        adjacent = [(i,j) for i,j
                    in map(lambda _x,_y: (_x,_y), 
                        (x, x, x + 1, x - 1), 
                        (y + 1, y - 1, y, y))
                    if 0 <= i < len(image)
                        and 0 <= j < len(image[i])
                        and image[i][j] == color]
        
        for pixel in adjacent:
            to_visit.append(pixel)
        
        # Flip current pixel
        image[x][y] = not color
        
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
