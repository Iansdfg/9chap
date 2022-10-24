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
    
    
 """
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        foundA, foundB, lca = self.dfs(root, A, B)
        return lca

    def dfs(self, root, A, B):
        #return foundA, foundB, lca
        if not root:
            return False, False, None 

        left_foundA, left_foundB, left_lca = self.dfs(root.left, A, B)
        right_foundA, right_foundB, right_lca= self.dfs(root.right, A, B)

        foundA = left_foundA or right_foundA or root == A 
        foundB = left_foundB or right_foundB or root == B

        lca = left_lca or right_lca
        if foundA and foundB:
            if not lca:
                lca = root
        else:
            lca = None 

        return foundA, foundB, lca
