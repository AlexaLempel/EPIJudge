from typing import List
from itertools import combinations

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    def is_valid_part(part: str) -> bool:
        return (part and part.isnumeric() 
                and (len(part) == 1 
                     or (part[0] != '0' and 1 <= int(part) <= 255)))
    
    if len(s) > 12 or len(s) < 4:
        return []
     
    result = []
    positions = range(len(s) + 3)
    dot_indices = combinations(positions, 3)

    for d1, d2, d3 in dot_indices:
        parts = (s[:d1], s[d1:d2], s[d2:d3], s[d3:])
        if all(map(is_valid_part, parts)):
            result.append(".".join(parts))
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
