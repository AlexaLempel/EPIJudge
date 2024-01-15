from collections import defaultdict, deque
from string import ascii_lowercase
from typing import Dict, Set

from test_framework import generic_test

def transform_string(D: Set[str], s: str, t: str) -> int:
    to_visit = deque([(s, 0)])
    D.remove(s)

    while to_visit:
        current, steps = to_visit.popleft()
        if current == t:
            return steps

        for idx in range(len(current)):
            for c in ascii_lowercase:
                word = current[:idx] + c + current[idx + 1:]
                if word in D:
                    D.remove(word)
                    to_visit.append((word, steps + 1))

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
