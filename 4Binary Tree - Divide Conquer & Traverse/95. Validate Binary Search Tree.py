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
        max_val, mini_val, valid = self.helper(root)
        return valid
        
    def helper(self, root):
        # return max_val, mini_val, valid
        if not root:
            return None, None, True 
            
        left_max_val, left_mini_val, left_valid = self.helper(root.left)
        right_max_val, right_mini_val, right_valid = self.helper(root.right)
        
        if not left_valid or not right_valid:
            return None, None, False 
        if left_max_val and left_max_val >= root.val:
            return None, None, False 
        if right_mini_val and right_mini_val <= root.val:
            return None, None, False 
        
        max_val = right_max_val if right_max_val else root.val
        mini_val = left_mini_val if left_mini_val else root.val
        
        return max_val, mini_val, True 
        
