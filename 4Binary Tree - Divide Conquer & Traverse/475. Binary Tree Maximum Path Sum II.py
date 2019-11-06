"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        # write your code here
        return self.helper(root)
        
    def helper(self, root):
        # return summ
        if not root:
            return 0
            
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
    
        result = max(left_sum + root.val, right_sum + root.val, root.val) 
        return result
        
        
