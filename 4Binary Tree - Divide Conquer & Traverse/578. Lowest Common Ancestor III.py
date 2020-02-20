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
        exist_A, exist_B, node_has_AorB = self.helper(root, A, B)
        return node_has_AorB if exist_A and exist_B else None
        
    def helper(self, root, A, B):
        # return exist_A, exist_B, node_has_AorB
        if not root:
            return False, False, None 
            
        left_exist_A, left_exist_B, left_node_has_AorB = self.helper(root.left, A, B)
        right_exist_A, right_exist_B, right_node_has_AorB = self.helper(root.right, A, B)
        
        exist_A = left_exist_A or right_exist_A or root == A
        exist_B = left_exist_B or right_exist_B or root == B
        
        if root == A or root == B:
            return exist_A, exist_B, root
        
        if left_node_has_AorB and right_node_has_AorB:
            return exist_A, exist_B, root 
        elif left_node_has_AorB:
            return exist_A, exist_B, left_node_has_AorB
        elif right_node_has_AorB:
            return exist_A, exist_B, right_node_has_AorB
        else:
            return exist_A, exist_B, None
            
