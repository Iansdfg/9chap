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
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder = []
        
        while stack:
            curr = stack.pop()
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
                    
            if stack:
                inorder.append(stack[-1].val)
                    
        return inorder
        
