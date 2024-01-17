from test_framework import generic_test


def divide(x: int, y: int) -> int:
    ans = 0
    shift = 64
    y_shift = y << shift
    
    while x >= y:
        while x < y_shift:
            y_shift = y_shift >> 1
            shift -= 1
        
        x -= y_shift
        ans += 1 << shift
    
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
