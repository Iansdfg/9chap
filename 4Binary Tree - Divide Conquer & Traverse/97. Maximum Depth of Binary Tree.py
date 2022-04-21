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
    @param root: The root of binary tree.
    @return: An integer
    """
    def max_depth(self, root):
        # write your code here
        return self.dfs(root)


    def dfs(self, root):
        if not root:
            return 0 

        left_h = self.dfs(root.left)
        right_h = self.dfs(root.right)

        return max(left_h, right_h) + 1 
