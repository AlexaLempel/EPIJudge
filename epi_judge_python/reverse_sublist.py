from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy_head = ListNode(0, L)
    prev = dummy_head
    
    # advance to the node before the start node
    for _ in range(1, start):
        prev = prev.next

    curr = prev.next
    for _ in range(finish - start):
        next = curr.next
        curr.next = next.next
        next.next = prev.next
        prev.next = next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
