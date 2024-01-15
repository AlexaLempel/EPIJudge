import functools
from collections import deque
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    def can_partition_bfs(vertex: GraphVertex) -> bool:
        vertex.d = 0
        to_visit = deque([vertex])

        while to_visit:
            current = to_visit.popleft()

            for edge in current.edges:
                if edge.d == current.d:
                    return False
                if edge.d == -1:
                    edge.d = not current.d
                    to_visit.append(edge)
        
        return True
    
    return all(can_partition_bfs(vertex) for vertex in graph if vertex.d == -1)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
