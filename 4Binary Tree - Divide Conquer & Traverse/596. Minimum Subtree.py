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
    @return: the root of the minimum subtree
    """
    min_sum, min_node = float('inf'), None
    
    def findSubtree(self, root):
        # write your code here
        self.helper(root)
        return self.min_node
        
    def helper(self, root):
        # return sum 
        if not root:
            return 0
            
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        sum_ = left_sum + right_sum + root.val 
        
        self.min_sum = min(self.min_sum, sum_)
        if sum_ == self.min_sum: 
            self.min_node = root
        
        return sum_
        
