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
    @return: true if it is a mirror of itself, or false.
    """
    def is_symmetric(self, root):
        # write your code here
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        if not l and not r:
            return True 
        
        if not l or not r:
            return False 

        if l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left):
            return True 
        
        return False 
        
