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
        self.dfs(root)

    def dfs(self, root):
        # return last right 
        if not root:
            return

        left_last = self.dfs(root.left)
        right_last = self.dfs(root.right)
        
        if left_last:
            left_last.right = root.right
            root.right =  root.left
            root.left = None

        return right_last or left_last or root
 

        


