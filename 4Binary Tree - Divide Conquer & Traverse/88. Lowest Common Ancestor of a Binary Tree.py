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
        if not root:
            return None
            
        if root == A or root == B:
            return root
    
        left_node = self.helper(root.left, A, B)
        right_node = self.helper(root.right, A, B)
        

        
        if left_node and right_node:
            return root
        elif left_node:
            return left_node
        elif right_node:
            return right_node
