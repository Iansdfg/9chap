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
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        upper, lower = root, root 
        curr = root 
        while curr:
            if curr.val > target:
                upper = curr
                curr = curr.left
            elif curr.val < target:
                lower = curr
                curr = curr.right
            else:
                return curr.val
        
        if abs(lower.val - target) > abs(upper.val - target):
            return upper.val
        else:
            return lower.val
