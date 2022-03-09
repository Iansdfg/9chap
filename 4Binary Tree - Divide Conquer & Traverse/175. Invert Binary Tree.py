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
        if not root:
            return 

        root.left, root.right = root.right, root.left
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)
