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
    @return: true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # write your code here
        if not root:
            return False 
            
        return self.helper(root.left, root.right)
        
    def helper(self, L, R):
        # return if left subtree and right subtree are symmetric
        if not L and not R:
            return True 
            
        if L and R and L.val == R.val:
            return self.helper(L.left,R.right) and self.helper(R.left,L.right)
        
        return False 
 
