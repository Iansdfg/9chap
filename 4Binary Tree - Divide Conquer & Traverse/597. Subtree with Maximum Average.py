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
    average, node = 0, None
    
    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.node
        
    def helper(self, root):
        # return # of node, avg 
        if not root:
            return 0, 0
            
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        
        
        summ = left_sum + right_sum + root.val
        size = left_size + right_size + 1
        
        if not self.node or summ / size > self.average:
            self.node = root
            self.average = summ * 1.0 / size
    
  
        return summ, size
        
        
        
