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


    def dfs(self, left, right):
        #return is left and left are euql 
        if not left and not right:
            return True 
            
        if not left or not right:
            return False

        if left.val == right.val:
            return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)

        return False 

