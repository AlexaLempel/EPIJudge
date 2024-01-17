from test_framework import generic_test


# def parity(x: int) -> int:
#     ans  = 0
#     while x:
#         x = x & (x - 1) # Flip right-most 1 to 0
#         ans = not ans
#     return ans


def parity(x: int) -> int:
    return x.bit_count() % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
