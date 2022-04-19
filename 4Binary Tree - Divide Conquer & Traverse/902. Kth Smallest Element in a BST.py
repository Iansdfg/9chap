from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root, k):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root 
        stack = [dummy]

        for _ in range(k + 1):
            curr = stack.pop()
            res = curr.val
            curr = curr.right
            while curr:
                stack.append(curr)
                curr = curr.left
        return res
