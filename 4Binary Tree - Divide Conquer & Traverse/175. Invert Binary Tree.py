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
    def invert_binary_tree(self, root: TreeNode):
        # write your code here

        self.dfs(root)
        return root


    def dfs(self, node):
        if not node:
            return None 

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        node.left, node.right = right, left

        return node 
