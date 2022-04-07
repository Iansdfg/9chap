"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:"""
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
        has_A, has_B, lca = self.dfs(root, A, B)
        if has_A and has_B:
            return lca
        return None

    def dfs(self, root, A, B):
        #has_A, has_B, lca(foundA or foundB)
        if not root:
            return False, False, None
        
        left_has_A, left_has_B, left_lca = self.dfs(root.left, A, B)
        right_has_A, right_has_B, right_lca = self.dfs(root.right, A, B)

        has_A = left_has_A or right_has_A or root == A
        has_B = left_has_B or right_has_B or root == B

        if root == A or root == B:
            return has_A, has_B, root 
        
        if left_lca and right_lca:
            return has_A, has_B, root 
        if left_lca:
            return has_A, has_B, left_lca 
        if right_lca:
            return has_A, has_B, right_lca 
        
        return has_A, has_B, None 


    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        has_A, has_B, LCA = self.dfs(root, A, B)
        if has_A and has_B:
            return LCA
        else:
            return None 
        
    def dfs(self, root, A, B):
        #has_A, has_B, LCA
        if not root:
            return False, False, None  

        left_has_A, left_has_B, left_LCA = self.dfs(root.left, A, B)
        right_has_A, right_has_B, right_LCA = self.dfs(root.right, A, B)
        
        a = left_has_A or right_has_A or A == root
        b = left_has_B or right_has_B or B == root

        if A == root or B == root:
            return a, b, root

        if left_LCA and right_LCA:
            return a, b, root
        if left_LCA:
            return a, b, left_LCA
        if right_LCA:
            return a, b, right_LCA
        
        return a, b, None

