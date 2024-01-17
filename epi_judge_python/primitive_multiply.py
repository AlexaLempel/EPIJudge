from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    def add(a: int, b: int) -> int:
        return a if not b else add(a ^ b, (a & b) << 1)
    
    answer = 0
    while y:
        if y & 1:
            answer = add(answer, x)
        x = x << 1
        y = y >> 1

    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
