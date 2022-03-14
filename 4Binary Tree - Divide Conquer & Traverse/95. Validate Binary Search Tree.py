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
        _, _, is_valid = self.helper(root)
        return is_valid
        
    def helper(self, root):
        # return max, min, valid 
        if not root:
            return None, None, True 
            
        left_max, left_min, left_valid = self.helper(root.left)
        right_max, right_min, right_valid = self.helper(root.right)
        
        if not left_valid or not right_valid:
            return None, None, False 
            
        if left_max and left_max >= root.val:
            return None, None, False 
            
        if right_min and right_min <= root.val:
            return None, None, False 
            
        min_val = left_min if left_min else root.val 
        max_val = right_max if right_max else root.val 
        
        return max_val, min_val, True

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
    @return: True if the binary tree is BST, or false
    """
    def is_valid_b_s_t(self, root):
        # write your code here
        max_val, min_val, is_valid = self.dfs(root)
        return is_valid

    def dfs(self, root):
        # return max, min, is_valid
        if not root:
            return float('-inf'), float('inf'), True
        
        left_max, left_min, left_is_valid = self.dfs(root.left)
        right_max, right_min, right_is_valid = self.dfs(root.right)
            
        max_val = max(right_max, root.val)
        min_val = min(left_min, root.val)

        is_valid = False
        if left_max < root.val and right_min > root.val:
            is_valid = right_is_valid and left_is_valid

        return max_val, min_val, is_valid



