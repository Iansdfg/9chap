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
        return self.is_valid(root.left, root.right)


    def is_valid(self, left, right):
        # return left and right child is symmetric
        if not left and not right:
            return True 

        if not left or not right:
            return False

        if left.val == right.val:
            return self.is_valid(left.left, right.right) and self.is_valid(left.right, right.left)

        return False


        

        

