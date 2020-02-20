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
    def invertBinaryTree(self, root):
        # write your code here
        return self.helper(root)
        
    def helper(self, root):
        if not root:
            return None
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        root.left = right
        root.right = left
        
        return root
        
        
        
