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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
            
        result = []
        self.helper(root, result)
        return result
        
    def helper(self, root, result):
        if not root:
            return
        
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)
        
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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        stack, res = [], []
        
        while root:
            stack.append(root)
            root = root.left
            
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
        return res
