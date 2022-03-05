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
        dummy = ListNode(0)
        last_node = None 
        res = []
        while queue:
            last_node = dummy

            for i in range(len(queue)):
                curr_tree = queue.popleft()
                node = ListNode(curr_tree.val)
                last_node.next = node
                last_node = last_node.next
                
                if curr_tree.left:
                    queue.append(curr_tree.left)
                if curr_tree.right:
                    queue.append(curr_tree.right)
            
            res.append(dummy.next)
        return res
