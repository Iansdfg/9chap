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
        res = None 
        while root:
            if root.val >= p.val:
                root = root.left 
            else:
                res = root
                root = root.right
        return res
    
    
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
        if not root:
            return root
        curr = root
        last = None
        
        while True:
            if curr == p:
                curr = curr.left
                
            if not curr:
                return last
            
            if curr.val > p.val:
                curr = curr.left
    
            else:
                last = curr 
                curr = curr.right
                
