"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if not self.check_exist(root, A) or not self.check_exist(root, B):
            return None
        return self.helper(root, A, B)
            
    def helper(self, root, A, B):
        if not root:
            return None 
        if root is A or root is B:
            return root
            
        left = self.helper(root.left, A, B)
        right = self.helper(root.right, A, B)
        
        if left and right:
            return root
        if not left and right:
            return right
        if not right and left:
            return left
        return None
        
    def check_exist(self, root, target):
        if not root:
            return False
        if root is target:
            return True
        return self.check_exist(root.left, target) or self.check_exist(root.right, target) 
        
