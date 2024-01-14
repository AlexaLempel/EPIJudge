import collections
import copy
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:

    def step_is_allowed(curr: Coordinate, next: Coordinate) -> bool:
        if not (0 <= next.x < len(maze) 
                and 0 <= next.y < len(maze[curr.x])
                and maze[next.x][next.y] == WHITE):
            return False
        
        return True
    
    def reachable(curr: Coordinate) -> Set[Coordinate]:
        return {coord for coord in map(Coordinate, 
            (curr.x, curr.x, curr.x - 1, curr.x + 1),
            (curr.y + 1, curr.y - 1, curr.y, curr.y))
            if step_is_allowed(curr, coord)}
        
    path = [s]
    curr = s
    visited = set()
    to_visit = collections.deque()
    
    while curr != e:
        visited.add(curr)
        candidates = reachable(curr) - visited    # O(1) for constant len(reachable)
        for space in candidates:
            to_visit.append(path + [space])   # Add to right side of queue
        
        if not to_visit:
            return []   # no solution
    
        path = to_visit.popleft()   # get next off left side of queue
        curr = path[-1]
    
    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
