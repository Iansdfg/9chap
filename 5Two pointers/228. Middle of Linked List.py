from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middle_node(self, head):
        # write your code here
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        return slow 
