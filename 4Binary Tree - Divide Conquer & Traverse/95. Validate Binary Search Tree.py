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
        max_num, min_num, is_bst = self.is_bst(root)
        return is_bst


    def is_bst(self, root):
        #Return max_num, min_num, is_bst 
        if not root:
            return float('-inf'), float('inf'), True, 
        
        left_max, left_min, left_is_bst = self.is_bst(root.left)
        right_max, right_min, right_is_bst = self.is_bst(root.right)

        is_bst = left_is_bst and right_is_bst and left_max < root.val  and root.val < right_min 

        max_num = max(root.val, left_max, right_max)
        min_num = min(root.val, left_min, right_min)

        return max_num, min_num, is_bst
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
    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        # write your code here
        valid, min_val, max_val  = self.dfs(root)
        return valid


    def dfs(self, node):
        if not node:
            return True, float('inf'), -float('inf') 

        left_valid, left_min, left_max= self.dfs(node.left)
        right_valid, right_min, right_max = self.dfs(node.right)

        valid = False
        if left_max < node.val and right_min > node.val:
            valid = left_valid and right_valid
        
        min_val = min(node.val, left_min)
        max_val = max(node.val, right_max)

        return valid, min_val, max_val 


