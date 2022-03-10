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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    node = None 
    min_val = float('inf')
    def find_subtree(self, root):
        # write your code here
        summ = self.dfs(root)
        return self.node

    def dfs(self, root):
        if not root:
            return 0
        
        left_sum, right_sum = self.dfs(root.left), self.dfs(root.right)
        curr_sum = left_sum + right_sum + root.val
        if curr_sum < self.min_val:
            self.min_val = curr_sum
            self.node = root
        return curr_sum
