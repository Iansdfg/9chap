"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if not head or not head.next:
            return None 
        
        slow = fast = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                break 

        if slow is fast:
            slow = head 
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast 

        return None 
