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
            
        stack = [root]
        pre_order = []
        
        while stack:
            curr = stack.pop()
            pre_order.append(curr.val)
            
            if curr.right:
                stack.append(curr.right)
                
            if curr.left:
                stack.append(curr.left)
                
        return pre_order
