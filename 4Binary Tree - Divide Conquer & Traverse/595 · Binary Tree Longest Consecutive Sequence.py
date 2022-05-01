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
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    max_val = 0
    def longest_consecutive(self, root):
        # write your code here
        self.dfs(root)
        return self.max_val


    def dfs(self, root):
        #return is_valid, max 
        if not root:
            return 0 

        left_len = self.dfs(root.left)
        right_len = self.dfs(root.right)

        left_valid = root.left and root.val + 1 == root.left.val
        right_valid = root.right and root.val + 1 == root.right.val

        if left_valid and right_valid:
            max_len = max(left_len, right_len) + 1

        elif left_valid:
            max_len = left_len + 1 

        elif right_valid:
            max_len = right_len + 1 
        
        else:
            max_len = 1

        self.max_val = max(self.max_val, max_len)
        return max_len


