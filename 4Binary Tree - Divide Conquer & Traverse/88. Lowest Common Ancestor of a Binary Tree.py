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
        if not root:
            return None
        LCA = self.helper(root, A, B)
        return LCA
        
    def helper(self, root, A, B):
        # return LCA
        if not root:
            return None 
            
        if root is A or root is B:
            return root
        
        left_LCA = self.helper(root.left, A, B)
        right_LCA = self.helper(root.right, A, B)
        
        if left_LCA and right_LCA:
            return root
        elif left_LCA:
            return left_LCA
        elif right_LCA:
            return right_LCA
        return None
