# Definition for singly-linked list.
from copy import copy
from typing import Optional
import queue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        nodes=queue.LifoQueue()
        new_head = ListNode(0, head)
        node = new_head
        final_next = None

        # Set this node.next to the first item in the current loop
        prev_loop_end_node = node

        # While nodes still exist keep process
        while node:
            x=1

            # Add nodes to lifo queue to flip order
            while nodes.qsize() < k:
                node = node.next

                if node is None:
                    break
                # Move first because initial pointer is the new head
                nodes.put(copy(node))

            if node is not None:
                # Keep this as an uneven amount of flip the last full loop will need a pointer to thenoraml list
                final_next = node.next

                while not nodes.empty():
                    prev_loop_end_node.next = nodes.get()
                    prev_loop_end_node = prev_loop_end_node.next

                node.next = final_next

        prev_loop_end_node.next = final_next
        return new_head.next


class Test:
    import pytest

    @pytest.mark.parametrize("head, k, expected",
                             [
                                 ([1,2,3,4,5], 3, [3,2,1,4,5]),
                                 ([1,2,3,4,5], 2, [2,1,4,3,5]),
                             ])
    def test(self, head, k, expected):
        # Create each of the linked lists
        prev = None
        for n in head[::-1]:
            prev = ListNode(n, prev)

        res = Solution().reverseKGroup(prev, k)

        i = 0
        while res:
            assert res.val == expected[i]
            res = res.next
            i+=1