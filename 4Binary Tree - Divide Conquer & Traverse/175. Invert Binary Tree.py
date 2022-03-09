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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invert_binary_tree(self, root):
        # write your code here
        if not root:
            return 

        root.left, root.right = root.right, root.left
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        
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
from collections import deque
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invert_binary_tree(self, root):
        # write your code here

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                
        return root

        
