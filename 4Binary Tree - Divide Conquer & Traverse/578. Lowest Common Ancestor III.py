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
        foundA, foundB, foundCandid = self.dfs(root, A, B)
        if foundA and foundB:
            return foundCandid
        return None 


    def dfs(self, root, A, B):
        #foundA, foundB, foundCandid

        if not root:
            return False, False, None

        left_foundA, left_foundB, left_foundCandid = self.dfs(root.left, A, B)
        right_foundA, right_foundB, right_foundCandid = self.dfs(root.right, A, B)


        foundA = left_foundA or right_foundA or root == A 
        foundB = left_foundB or right_foundB or root == B 

        if root == A or root == B:
            return foundA, foundB, root

        if left_foundCandid and right_foundCandid:
            return foundA, foundB, root
        if left_foundCandid:
            return foundA, foundB, left_foundCandid
        if right_foundCandid:
            return foundA, foundB, right_foundCandid
        
        return foundA, foundB, None 
