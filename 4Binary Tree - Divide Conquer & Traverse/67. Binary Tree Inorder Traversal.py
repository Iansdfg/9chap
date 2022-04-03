from lintcode import (
    TreeNode,
)

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
    def inorder_traversal(self, root):
        # write your code here
        dummy = TreeNode(-1)
        dummy.right = root
        stack = [dummy]
        inorder = []
        while stack:
            curr = stack.pop()
            if curr.right:
                curr = curr.right
                stack.append(curr)
                
                while curr.left:
                    curr = curr.left
                    stack.append(curr)

            if stack:
                inorder.append(stack[-1].val)

        return inorder
        
           
 ################## if not use dummy ##################
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root):
        # write your code here
        stack = []
        while root:
            stack.append(root)
            root = root.left
        inorder = []

        while stack:
            curr = stack.pop()
            inorder.append(curr.val)
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left

        return inorder
