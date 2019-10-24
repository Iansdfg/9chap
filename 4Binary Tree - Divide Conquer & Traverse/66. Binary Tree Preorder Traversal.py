"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        result = []
        self.helper(root, result)
        return result
        
    def helper(self, root, result):
        if not root:
            return
        result.append(root.val)
        self.helper(root.left, result)
        self.helper(root.right, result)
