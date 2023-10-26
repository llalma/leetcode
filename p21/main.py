# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head

        # While either still has a value
        while list1 or list2:
            if list1 is None or (list2 is not None and list1.val > list2.val):
                node.next = list2
                list2 = list2.next
            else:
                node.next=list1
                list1 = list1.next

            node = node.next

        # Move 1 position forward as first node is blank
        return head.next
class Test:
    import pytest

    @pytest.mark.parametrize("list1, list2, expected",
                             [
                                 ([1], [], [1]),
                                 ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
                                 ([], [], []),
                                 ([], [0], [0]),
                             ])
    def test(self, list1, list2, expected):
        list1_1 = None
        for v in list1[::-1]:
            list1_1 = ListNode(v,list1_1)
        list2_1 = None
        for v in list2[::-1]:
            list2_1 = ListNode(v, list2_1)
        expected_1 = None
        for v in expected[::-1]:
            expected_1 = ListNode(v, expected_1)

        res = Solution().mergeTwoLists(list1_1, list2_1)

        while res:
            assert res.val == expected_1.val
            res = res.next
            expected_1 = expected_1.next