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
    mini = float('inf')
    mini_node = None 
    
    def findSubtree(self, root):
        # write your code here
        self.helper(root)
        return self.mini_node
        
    def helper(self, root):
        #  return sum
        if not root:
            return 0
            
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        
        summ = left_sum + right_sum + root.val
        if summ < self.mini:
            self.mini = summ
            self.mini_node = root
  
        return summ
        
        
        
