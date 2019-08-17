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
        isBST, minNode, maxNode = self.divideConquer(root)
        return isBST
        
    def divideConquer(self, root):
        if not root:
            return True, None, None
            
        left_isBST, left_minNode, left_maxNode = self.divideConquer(root.left)
        right_isBST, right_minNode, right_maxNode = self.divideConquer(root.right)
        
        if not left_isBST or not right_isBST: 
            return False, None, None
        if left_maxNode and left_maxNode>= root.val:
            return False, None, None
        if right_minNode and right_minNode<= root.val:
            return False, None, None
        
        minNode = left_minNode if left_minNode else root.val
        maxNode = right_maxNode if right_maxNode else root.val
        
        return True, minNode, maxNode
