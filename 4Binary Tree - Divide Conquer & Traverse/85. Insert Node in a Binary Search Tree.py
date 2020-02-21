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
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        head = dummy = TreeNode(float('-inf'))
        dummy.right = root
        
        while root:
            dummy = root
            if node.val > dummy.val:
                root = root.right
            elif node.val < root.val:
                root = root.left
                
        if node.val > dummy.val:
            dummy.right = node
        else:
            dummy.left = node
        
        return head.right
            
