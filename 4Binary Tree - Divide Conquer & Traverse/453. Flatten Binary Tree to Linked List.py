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
    def flatten(self, root):
        # write your code here
        return self.dfs(root)

    def dfs(self, root):
        #return root 
        if not root:
            return None 

        left_child = self.dfs(root.left)
        right_child = self.dfs(root.right)

        if not left_child:
            return root

        #find left end 
        left_end = left_child
        while left_end and left_end.right:
            left_end = left_end.right

        #flatten
        root.left = None
        root.right = left_child
        left_end.right = right_child

        return root


