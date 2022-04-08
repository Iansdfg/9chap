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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
	   fast = slow = head

	   while fast.next and fast.next.next:
		   fast = fast.next.next
		   slow = slow.next
		   
		   if slow == fast:
			   return True 
	   return False 


