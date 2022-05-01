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
max_len = 0
max_dec = 0
max_inc = 0
class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    max_len = 0
    def longest_consecutive2(self, root):
        # write your code here
        self.dfs(root)
        return self.max_len


    def dfs(self, root):
        if not root:
            return 0, 0
        
        left_inc, left_dec  = self.dfs(root.left)
        right_inc, right_dec = self.dfs(root.right)

        is_left_dec = root.left and root.left.val + 1 == root.val 
        is_left_inc= root.left and root.left.val - 1 == root.val 

        is_right_dec = root.right and root.right.val + 1 == root.val 
        is_right_inc = root.right and root.right.val - 1 == root.val 

        if is_left_dec and is_right_dec:
            dec_len = max(left_dec, right_dec) + 1 
        elif is_left_dec:
            dec_len = left_dec + 1
        elif is_right_dec:
            dec_len = right_dec + 1
        else:
            dec_len = 1

        if is_left_inc and is_right_inc:
            inc_len = max(left_inc, right_inc) + 1 
        elif is_left_inc:
            inc_len = left_inc + 1
        elif is_right_inc:
            inc_len = right_inc + 1
        else:
            inc_len = 1

        self.max_len = max(self.max_len, inc_len + dec_len - 1)
        return inc_len, dec_len




