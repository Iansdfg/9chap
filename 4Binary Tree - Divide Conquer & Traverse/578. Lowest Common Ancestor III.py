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
        has_A, has_B, node_has_A_or_B = self.helper(root, A, B)
        return node_has_A_or_B if has_A and has_B else None 
        
        
    def helper(self, root, A, B):
        # return has_A, has_B, node_has_A_or_B
        if not root:
            return False, False, None
            
        left_has_A, left_has_B, left_has_A_or_B = self.helper(root.left, A, B)
        right_has_A, right_has_B, right_has_A_or_B = self.helper(root.right, A, B)
        
        has_A = left_has_A or right_has_A or root == A 
        has_B = left_has_B or right_has_B or root == B  
        
        if root == A or root == B: 
            return has_A, has_B, root 
        
        if left_has_A_or_B and right_has_A_or_B:
            return has_A, has_B, root 
            
        if left_has_A_or_B:
            return has_A, has_B, left_has_A_or_B 
            
        if right_has_A_or_B:
            return has_A, has_B, right_has_A_or_B 
            
        return has_A, has_B, None  
            
            
            
            
            
            
            
        
        
