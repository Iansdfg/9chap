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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root, target):
        # write your code here
        higher, lower = root.val, root.val

        while root:
            if root.val > target:
                higher = root.val
                root = root.left 
            elif root.val < target:
                lower = root.val
                root = root.right 
            else:
                return root.val
        if abs(lower - target) > abs(higher - target):
            return higher
        else:
            return lower

        
