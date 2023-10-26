# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        head = node = ListNode()

        # Find list of nodes and values
        values = [(n.val, n) for n in lists if n]

        # While any of them have a value
        while len(values)>0:

            # Get the min index
            min_index = values.index(min(values, key=lambda x: x[0]))

            node.next = values[min_index][1]
            node = node.next

            # Check if just added node has a next position
            if values[min_index][1].next is None:
                del values[min_index]
            else:
                # Move min node to next position
                values[min_index] = (values[min_index][1].next.val, values[min_index][1].next)


        # Skip first one as its blank
        return head.next
class Test:
    import pytest

    @pytest.mark.parametrize("lists, expected",
                             [
                                 ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
                                 ([], []),
                                 ([[]], []),
                             ])
    def test(self, lists, expected):
        # Create each of the linked lists
        heads=[]
        for l in lists:
            prev = None
            for n in l[::-1]:
                prev = ListNode(n, prev)
            heads.append(prev)

        res = Solution().mergeKLists(heads)

        i = 0
        while res:
            assert res.val == expected[i]
            res = res.next
            i+=1