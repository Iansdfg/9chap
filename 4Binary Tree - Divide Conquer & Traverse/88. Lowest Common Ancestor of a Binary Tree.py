
    
 """
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

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
        found_A, found_B, LCA = self.dfs(root, A, B)
        return LCA

    def dfs(self, node, A, B):
        # return find_A, find_B, find_lca
        if not node:
            return False, False, None 


        left_found_A, left_found_B, left_LCA = self.dfs(node.left, A, B)
        right_found_A, right_found_B, right_LCA = self.dfs(node.right, A, B)

        found_A, found_B = False, False

        if node == A or left_found_A or right_found_A:
            found_A = True 
        if node == B or left_found_B or right_found_B:
            found_B = True
        
        LCA = None 
        if found_A and found_B:
            LCA = node
        if left_LCA or right_LCA:
            LCA = left_LCA or right_LCA
        # print(node.val, found_A, found_B, LCA.val if LCA else 'N')
        return found_A, found_B, LCA
        
