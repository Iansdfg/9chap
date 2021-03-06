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
        result = []
        while queue:
            head = curr = ListNode(0)
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.next = ListNode(node.val)
                curr = curr.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(head.next)
        return result 
