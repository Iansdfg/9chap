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
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root):
        # write your code here
        return self.dfs(root)

    def dfs(self, root):
        #retrun minial depth
        if not root:
            return 0

        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)
        
        if not left_depth and not right_depth:
            depth = 1 
        elif left_depth and right_depth:
            depth = min(left_depth, right_depth) + 1
        else:
            depth = (left_depth or right_depth) + 1 
        return depth
