"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""

from collections import deque
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root: return {}
        queue = deque([root])
        res = []
        while queue:
            dummy_head = ListNode(-1)
            pointer = dummy_head

            for i in range(len(queue)):
                curr = queue.popleft()
                pointer.next = ListNode(curr.val)
                pointer = pointer.next
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(dummy_head.next)
        return res




