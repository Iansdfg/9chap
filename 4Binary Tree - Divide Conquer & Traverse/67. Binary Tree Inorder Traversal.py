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
        if not root: return []
        dummy = TreeNode(0)
        dummy.right = root
        result, stack = [], [dummy]
        
        while stack:
            curr = stack.pop()
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
            if stack:
                result.append(stack[-1].val)
        return result 
                    
            
