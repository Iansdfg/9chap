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
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root):
        # write your code here
        is_balanced, hight = self.dfs(root)
        return is_balanced

    def dfs(self, root):
        #is_balanced, hight 
        if not root:
            return True, 0

        left_balanced, left_h = self.dfs(root.left)
        right_balanced, right_h = self.dfs(root.right)

        is_balanced = left_balanced and right_balanced and abs(left_h - right_h) <= 1 

        hight = max(left_h, right_h) + 1 

        return is_balanced, hight

