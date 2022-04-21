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
    @param root: the root of binary tree.
    @return: An integer
    """
    max_val = float('-inf')
    def max_path_sum2(self, root):
        # write your code here
        self.dfs(root, root.val)
        return self.max_val


    def dfs(self, root, summ):
        if summ > self.max_val:
            self.max_val = summ

        for next_node in [root.left, root.right]:
            if not next_node:
                continue
            summ += next_node.val
            self.dfs(next_node, summ)
            summ -= next_node.val
