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
    max_val = float('-inf')
    def max_path_sum(self, root):
        # write your code here
        max_path_sum = self.dfs(root)
        return self.max_val


    def dfs(self, root):
        #retrn max_path_sum 
        if not root:
            return 0 

        left_path_sum = self.dfs(root.left)
        right_path_sum = self.dfs(root.right)

        max_path_sum = max(left_path_sum + root.val, right_path_sum + root.val, root.val, 0)
        self.max_val = max(self.max_val, root.val + left_path_sum + right_path_sum, root.val + left_path_sum, root.val + right_path_sum)

        return max_path_sum


