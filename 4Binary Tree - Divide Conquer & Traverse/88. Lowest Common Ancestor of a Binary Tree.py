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
        return self.helper(root, A, B)
        
    def helper(self, root, A, B):
        # return node_has_AorB
        if not root:
            return None 
            
        left_node_has_AorB = self.helper(root.left, A, B)
        right_node_has_AorB = self.helper(root.right, A, B)
        
        if root == A or root == B:
            return root 
            
        if left_node_has_AorB and right_node_has_AorB:
            return root
        elif left_node_has_AorB:
            return left_node_has_AorB
        elif right_node_has_AorB:
            return right_node_has_AorB
        else:
            return None 
        
        
        
