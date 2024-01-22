from test_framework import generic_test
from functools import reduce
from string import hexdigits

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def base_str_to_int(num_as_str: str, base: int) -> int:
        is_neg = num_as_str[0] == '-'
        result = reduce(lambda num, c: num * base + hexdigits.index(c.lower()), num_as_string[is_neg:], 0)
        return result * -1 if is_neg else result
    
    if num_as_string == '0':
        return '0'
    
    num_as_int = base_str_to_int(num_as_string, b1)
    is_neg = num_as_int < 0
    if is_neg: 
        num_as_int *= -1

    result = []
    while num_as_int:
        result.append(hexdigits[(num_as_int % b2)].upper())
        num_as_int //= b2
    
    return ('-' if is_neg else '') + "".join(reversed(result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
