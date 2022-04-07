
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if not p or not q:
            return None 
            
        lca = self.helper(root, p, q)
        return lca
        
        
    def helper(self, root, p, q):
        if not root:
            return None 
            
        p_val, q_val = p.val, q.val
        
        if p_val == root.val or q_val == root.val:
            return root
        
        if min(p_val, q_val) < root.val <  max(p_val, q_val):
            return root
        elif root.val <= min(p_val, q_val):
            return self.helper(root.right, p, q)
        elif root.val >= max(p_val, q_val):
            return self.helper(root.left, p, q)
            
            
