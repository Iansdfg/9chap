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
    def isBalanced(self, root):
        # write your code here
        hight, is_balanced = self.helper(root)
        return is_balanced
        
    def helper(self, root):
        # return hight, is_balanced
        if not root:
            return 0, True
            
        left_hight, left_is_balanced = self.helper(root.left)
        right_hight, right_is_balanced = self.helper(root.right)
        
        if not left_is_balanced or not right_is_balanced:
            return 0, False 
        
        hight = max(left_hight, right_hight) + 1 
            
        is_balanced = True if abs(left_hight - right_hight) <= 1 else False
        
        return hight, is_balanced
