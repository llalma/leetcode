# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_node = ListNode(0, head)

        prev_node = head_node
        node = head_node.next

        while node:
            if node.next:
                prev_node.next=node.next
                node.next = node.next.next
                prev_node.next.next = node

            prev_node = node
            node = node.next


        return head_node.next

class Test:
    import pytest

    @pytest.mark.parametrize("head, expected",
                             [
                                 ([1,2,3,4], [2,1,4,3]),
                                 ([], []),
                                 ([1], [1]),
                             ])
    def test(self, head, expected):
        # Create each of the linked lists
        prev = None
        for n in head[::-1]:
            prev = ListNode(n, prev)

        res = Solution().swapPairs(prev)

        i = 0
        while res:
            assert res.val == expected[i]
            res = res.next
            i+=1