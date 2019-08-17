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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        balaced, _ = self.valid(root)
        return balaced
        
        
    def valid(self, root):
        if not root:
            return True, 0
            
        balaced, left_hight = self.valid(root.left)
        if not balaced:
            return False, 0
            
        balaced, right_hight = self.valid(root.right)
        if not balaced:
            return False, 0
        
        return abs(left_hight-right_hight)<=1, max(left_hight, right_hight)+1
        
            
        
        
