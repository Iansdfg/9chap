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
        lca = self.helper(root, A, B)
        return lca 
        
    def helper(self, root, A, B):
        # return lca
        if not root:
            return None 
        
        if root == A or root == B :
            return root
            
        left = self.helper(root.left, A, B)
        right = self.helper(root.right, A, B)
        
        if left and right:
            return root
            
        if left:
            return left
            
        if right:
            return right
            
        return None 
