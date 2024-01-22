from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L or not L.next or not L.next.next:
        return L
    
    curr_even = L
    curr_odd = L.next
    evens_dummy = ListNode(0, curr_even)
    odds_dummy = ListNode(0, curr_odd)
    is_even = True

    while curr_even.next and curr_odd.next:
        if is_even:  # process next even
            curr_even.next = curr_odd.next
            curr_even = curr_even.next
        else:   #process next odd
            curr_odd.next = curr_even.next
            curr_odd = curr_odd.next
        is_even = not is_even
    
    if is_even: # even, odd remain
        curr_even.next = None
    else:   # odd, even remain
        curr_odd.next = None

    curr_even.next = odds_dummy.next

    return evens_dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
