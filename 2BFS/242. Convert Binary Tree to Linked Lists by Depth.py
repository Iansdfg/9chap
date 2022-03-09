"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
from collections import deque
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
        queue = deque([root])
        dummy = ListNode(-1)
        last = None 
        res = []
        while queue:
            last = dummy
            for i in range(len(queue)):
                curr = queue.popleft()
                new_node = ListNode(curr.val)
                last.next = new_node
                last = last.next
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(dummy.next)
        return res
            
                






