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
        return root
        
    def helper(self, root):
        # return last node 
        if not root:
            return None 
            
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        if not left_last and not right_last:
            return root
        
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None 
            
        if right_last:
            return right_last
        else:
            return left_last
            
