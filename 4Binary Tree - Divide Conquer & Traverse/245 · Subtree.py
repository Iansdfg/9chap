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
    @param t1: The roots of binary tree T1.
    @param t2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def is_subtree(self, t1, t2):
        # write your code here
        if not t2:
            return True
        return self.dfs(t1, t2)
        
    def dfs(self, t1, t2):
        if t1 == None:
            return t2 == None

        if t1.val == t2.val and self.is_same_tree(t1, t2):
            return True 

        left_is_subtree = self.dfs(t1.left, t2)
        right_is_subtree = self.dfs(t1.right, t2)

        if left_is_subtree or right_is_subtree:
            return True 
        return False 

    def is_same_tree(self, t1, t2):
        #return is_same_tree
        if t1 == None and t2 == None:
            return True 

        if t1 == None or t2 == None:
            return False

        left_is_same = self.is_same_tree(t1.left, t2.left)
        right_is_same = self.is_same_tree(t1.right, t2.right)

        if left_is_same and right_is_same and t1.val == t2.val:
            return True 

        return False 
