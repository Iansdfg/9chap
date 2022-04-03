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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invert_binary_tree(self, root):
        # write your code here
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return None 

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        root.left, root.right = right, left

        return root
