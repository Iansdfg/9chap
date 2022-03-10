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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root):
        # write your code here
        if not root:
            return []
        stack = [root]
        order = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            order.append(node.val)
            
            stack.append(node.right)
            stack.append(node.left)
        return order

