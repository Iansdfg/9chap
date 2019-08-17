"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        self.is_valid = True
        self.lastVal = None
        self.pre_order(root)
        return self.is_valid
        
    def pre_order(self, root):
        if not root:
            return
        self.pre_order(root.left)
        if self.lastVal and root.val and root.val<=self.lastVal:
            self.is_valid = False
            return
        self.lastVal = root.val
        self.pre_order(root.right)
