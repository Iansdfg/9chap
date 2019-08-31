"""
Definition of ListNode
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
    def middleNode(self, head):
        # write your code here
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
