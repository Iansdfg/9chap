"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
	   return self.dfs(head)

    def dfs(self, head):
	    if not head: 
		    return None
		# if there is only on node in the list, return it 
	    if not head.next:
		    return TreeNode(head.val)

	    pre, mid = self.find_middle(head)
	    pre.next = None 
	
	    root = TreeNode(mid.val)
	    left_head = head
	    right_head = mid.next
	    root.left = self.dfs(left_head)
	    root.right = self.dfs(right_head)

	    return root
	    
    def find_middle(self, head):
	   slow, fast = head, head
	   dummy = ListNode(0)
	   dummy.next = head
	   while fast and fast.next:
		   dummy = dummy.next
		   slow = slow.next
		   fast = fast.next.next
	   return dummy, slow

