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
        if not root:
            return None 
            
        A_exist, B_exist, LCA = self.helper(root, A, B)
        if A_exist and B_exist:
            return LCA
        else:
            return None
     
    def helper(self, root, A, B):
        # return A_exist, B_exist, LCA
        if not root:
            return False, False, None
            
        left_A_exist, left_B_exist, left_LCA = self.helper(root.left, A, B)
        right_A_exist, right_B_exist, right_LCA = self.helper(root.right, A, B)
        
        A_exist = left_A_exist or right_A_exist or root is A
        B_exist =  left_B_exist or right_B_exist or root is B
        
        if A == root or B == root:
            return A_exist, B_exist, root
  
        if right_LCA and left_LCA:
            return A_exist, B_exist, root
        elif right_LCA:
            return A_exist, B_exist, right_LCA
        elif left_LCA:
            return A_exist, B_exist, left_LCA
        return A_exist, B_exist, None
