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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        # write your code here
        h, is_balanced = self.dfs(root)
        return is_balanced

    def dfs(self, node):
        # return h, is_balanced 
        if not node:
            return 0, True 

        left_h, left_is_balanced = self.dfs(node.left)
        right_h, right_is_balanced = self.dfs(node.right)

        is_balanced = False 
        
        if abs(left_h - right_h) <= 1 and left_is_balanced and right_is_balanced:
            is_balanced = True 

        
        
        return max(left_h, right_h) + 1, is_balanced

