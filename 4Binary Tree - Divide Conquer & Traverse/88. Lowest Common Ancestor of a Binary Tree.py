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
        return self.dfs(root, A, B)

    def dfs(self, root, A, B):
        if not root:
            return None 

        if root == A or root == B:
            return root

        found_left = self.dfs(root.left, A, B)
        found_right = self.dfs(root.right, A, B)

        if found_left and found_right:
            return root 
        if found_left:
            return found_left
        if found_right:
            return found_right
        if not found_right and not found_left:
            return None 
        return None 


