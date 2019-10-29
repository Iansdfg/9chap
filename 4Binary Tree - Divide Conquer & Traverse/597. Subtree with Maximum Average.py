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
    @return: the root of the maximum average of subtree
    """
    max_avg_node = None
    max_ave = float('-inf')
    
    
    def findSubtree2(self, root):
        # write your code here
        summ, size = self.helper(root)
        return self.max_avg_node
        
     
    def helper(self, root):
        # return summ, size
        if not root:
            return 0, 0
        
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        
        summ =  left_sum + right_sum + root.val
        size = left_size + right_size + 1
        
        if summ / size > self.max_ave: 
            self.max_ave = summ / size
            self.max_avg_node = root

        return summ, size
