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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        min_val, max_val, valid = self.helper(root)
        return valid
        
    def helper(self, root):
        # return min, max, valid 
        if not root:
            return None, None, True 
            
        left_min, left_max, left_valid = self.helper(root.left)
        right_min, right_max, right_valid = self.helper(root.right)
        
        if not left_valid or not right_valid:
            return None, None, False 
            
        if left_max and left_max >= root.val:
            return None, None, False 
            
        if right_min and right_min <=root.val:
            return None, None, False 
        
        min_val = left_min if left_min else root.val
        max_val = right_max if right_max else root.val
        
        return min_val, max_val, True
