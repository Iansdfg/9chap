"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        return  self.helper(root, A, B)
        
        
    def helper(self, root, A, B):
        # return node has A or B  
        
        if not root:
            return None
        
        left = self.helper(root.left, A, B)
        right = self.helper(root.right, A, B)
        
        
        if root == A or root == B:
            return root 
            
        elif left and right:
            return root
        
        elif left:
            return left
        elif right:
            return right
            
            
