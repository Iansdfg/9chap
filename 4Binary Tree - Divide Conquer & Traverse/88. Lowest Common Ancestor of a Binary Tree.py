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
        # return node has A or B 
        if not root:
            return None 
            
        if root == A or root == B:
            return root 
        
        left_has_A_or_B = self.helper(root.left, A, B)
        right_has_A_or_B = self.helper(root.right, A, B)
        
        if left_has_A_or_B and right_has_A_or_B:
            return root
        elif left_has_A_or_B:
            return left_has_A_or_B
        elif right_has_A_or_B:
            return right_has_A_or_B
        
       
