"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if  not root:
            return 0
        return self.helper(root)
        
        
    def helper(self, root):
        # return mini_len
        if not root.left and not root.right:
            return 1
            
        left_len = self.helper(root.left) if root.left else float("inf")
        right_len = self.helper(root.right) if root.right else float("inf")
        
        return min(left_len, right_len) + 1
