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
        has_A, has_B, node_has_AorB = self.helper(root, A, B)
        
        if has_A and has_B:
            return node_has_AorB
        return None 
        
        
    def helper(self, root, A, B):
        # return has_A, has_B, node_has_AorB
        if not root:
            return False, False, None 
            
        left_has_A, left_has_B, left_node_has_AorB = self.helper(root.left, A, B)
        right_has_A, right_has_B, right_node_has_AorB = self.helper(root.right, A, B)
        
        has_A = left_has_A or right_has_A or A == root
        has_B = left_has_B or right_has_B or B == root 
        
        if root == A or root == B:
            return has_A, has_B, root
        
        elif left_node_has_AorB and right_node_has_AorB:
            return has_A, has_B, root 
            
        elif left_node_has_AorB:
            return has_A, has_B, left_node_has_AorB
            
        elif right_node_has_AorB:
            return has_A, has_B, right_node_has_AorB
            
        return has_A, has_B, None 
        
        
