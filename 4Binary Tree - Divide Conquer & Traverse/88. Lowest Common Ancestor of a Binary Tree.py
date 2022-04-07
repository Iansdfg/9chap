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
        lca = self.dfs(root, p, q)
        return lca


    def dfs(self, root, p, q):
        #return cadidit 
        if not root:
            return None 

        left_cand = self.dfs(root.left, p, q)
        right_cand =  self.dfs(root.right, p, q)

        if root == q or root == p:
            return root 

        if left_cand and right_cand:
            return root 
        if left_cand:
            return left_cand
        if right_cand:
            return right_cand
        return None 
