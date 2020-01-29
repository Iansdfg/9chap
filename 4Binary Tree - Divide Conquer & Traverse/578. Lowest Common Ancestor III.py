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
        has_A, has_B, lca  = self.helper(root, A, B)
        
        return lca 
        
        
    def helper(self, root, A, B):
        # return has_A, has_B, lca 
        if not root:
            return False, False, None 
            
        left_has_A, left_has_B, left_lca = self.helper(root.left, A, B)
        right_has_A, right_has_B, right_lca = self.helper(root.right, A, B)
        
        has_A = left_has_A or right_has_A or A == root 
        has_B = left_has_B or right_has_B or B == root
        
        if has_A and has_B:
            if left_lca and not right_lca:
                return has_A, has_B, left_lca
            elif right_lca and not left_lca:
                return has_A, has_B, right_lca
            else:
                return has_A, has_B, root
        else:
            return has_A, has_B, None 
