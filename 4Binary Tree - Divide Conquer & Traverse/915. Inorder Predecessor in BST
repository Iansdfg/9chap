"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        ans = None 
        
        while root:
            if root.val > p.val:
                root = root.left
            
            elif root.val == p.val:
                root = root.left
            
            elif root.val < p.val:
                if not ans or ans.val < root.val:
                    ans = root
                root = root.right
                
        return ans
