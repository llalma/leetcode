# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def _solve(self, node):

        # Check if end of list
        if node is None:
            return None

        node_ahead = self._solve(node.next)
        node.next = node_ahead
        self.n -= 1

        if self.n == 0:
            return node_ahead
        return node


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.n = n
        return self._solve(head)



class Test:
    import pytest

    @pytest.mark.parametrize("head, n, expected",
                             [
                                 ([1,2], 2, [2]),
                                 ([1,2,3,4,5], 5, [2,3,4,5]),
                                 ([1,2,3,4,5], 2, [1,2,3,5]),
                                 ([1], 1, []),
                                 ([1,2], 1, [1])
                             ])
    def test(self, head, n, expected):
        # Create the ListNode objects
        prev_node = None
        for v in head[::-1]:
            prev_node = ListNode(v, prev_node)

        assert  Solution().removeNthFromEnd(prev_node, n) == expected