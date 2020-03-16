"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        
        self.helper(root)
        
        
    def helper(self, root):
        # return last_node 
        
        if not root:
            return None 
            
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        if not left_last and not right_last:
            return root
            
        if not left_last:
            return right_last
            
        left = root.left
        right = root.right
        
        if not right_last:
            root.right = left
            root.left = None
            return left_last
        
        left_last.right = right
        root.right = left
        root.left = None
        return right_last
        
        
        
        
        
        
