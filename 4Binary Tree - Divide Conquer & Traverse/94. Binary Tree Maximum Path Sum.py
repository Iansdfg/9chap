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
    def max_path_sum(self, root):
        # write your code here
        max_all, max_path = self.dfs(root)
        return max_all

    

    def dfs(self, root):
        #return max_all, max_path
        if not root:
            return float('-inf'), 0

        left_max_all, left_max_path = self.dfs(root.left)
        right_max_all, right_max_path = self.dfs(root.right)

        max_path = max(root.val + left_max_path, root.val + right_max_path, 0)
        max_all = max(left_max_all, right_max_all, left_max_path + right_max_path + root.val)

        return max_all, max_path

        
