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
    avg = 0
    max_node = None
    
    def findSubtree2(self, root):
        # write your code here
        if not root: return None 
        self.hlper(root)
        return self.max_node
    
    def hlper(self, root):
        # return summ, size 
        if not root:
            return 0, 0 
            
        left_sum, left_size  = self.hlper(root.left)
        right_sum, right_size = self.hlper(root.right)
        
        summ = left_sum + right_sum + root.val
        size = left_size + right_size + 1
        
        if self.max_node == None or summ / size > self.avg:
            self.avg = summ / size
            self.max_node = root

        return summ, size
