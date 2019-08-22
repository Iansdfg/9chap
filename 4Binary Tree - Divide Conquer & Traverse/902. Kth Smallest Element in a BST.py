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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here

        res  = []
        self.save(root,res)
        return res[k-1]
        
        
    def save(self,root,res):
        if not root:
            return
        self.save(root.left,res)
        res.append(root.val)
        self.save(root.right,res)
        
        
        
