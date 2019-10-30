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
        max_val, min_val, valid  = self.hleper(root)
        return valid

        
    def hleper(self, root):
        # return max_val, min_val, valid 
        if not root:
            return None, None, True
            
        letf_max_val, letf_min_val, letf_valid = self.hleper(root.left)
        right_max_val, right_min_val, right_valid = self.hleper(root.right)
        
        if not letf_valid or not right_valid: 
            return None, None, False
        if letf_max_val and letf_max_val >= root.val:
            return None, None, False
        if right_min_val and right_min_val <= root.val:
            return None, None, False
            
        max_val = right_max_val if right_max_val else root.val
        mini_val = letf_min_val if letf_min_val else root.val
        
        return max_val, mini_val, True
