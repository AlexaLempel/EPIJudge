from test_framework import generic_test
from functools import lru_cache

@lru_cache(None)
def look_and_say(n: int) -> str:
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    
    prev = look_and_say(n - 1)
    curr = prev[0]
    count = 1
    result = []
    for c in prev[1:]:
        if c == curr: 
            count += 1
        else:
            result.append(str(count) + curr)
            curr = c
            count = 1
    
    result.append(str(count) + curr)
    
    return ''.join(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
