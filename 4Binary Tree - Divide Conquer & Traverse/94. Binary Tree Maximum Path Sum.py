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
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        max_path_sum, single_path_sum = self.helper(root)
        return max_path_sum
        
        
        
    def helper(self, root):
        # return max_path_sum,single_path_sum
        if not root:
            return float('-inf'), 0
            
        left_max_path_sum, left_single_path_sum =  self.helper(root.left)
        right_max_path_sum, right_single_path_sum =  self.helper(root.right)
        
        
        
        max_path_sum = max(left_max_path_sum, right_max_path_sum, root.val + left_single_path_sum + right_single_path_sum)
        
        single_path_sum = max(right_single_path_sum + root.val, left_single_path_sum + root.val, 0)
        
        return max_path_sum, single_path_sum
