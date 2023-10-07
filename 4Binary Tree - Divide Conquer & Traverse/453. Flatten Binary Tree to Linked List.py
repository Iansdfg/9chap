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
    def flatten(self, root):
        # write your code here
        return self.dfs(root)

    def dfs(self, root):
        #return root 
        if not root:
            return None 

        left_child = self.dfs(root.left)
        right_child = self.dfs(root.right)

        if not left_child:
            return root

        #find left end 
        left_end = left_child
        while left_end and left_end.right:
            left_end = left_end.right

        #flatten
        root.left = None
        root.right = left_child
        left_end.right = right_child

        return root

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
    def flatten(self, root: TreeNode):
        # write your code here
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        left_end = left
        while left_end and left_end.right:
            left_end = left_end.right

        if left_end:
            left_end.right = right
            root.right = left 
            root.left = None

        return root

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
    def flatten(self, root: TreeNode):
        # write your code here
        return self.dfs(root)



    def dfs(self, node):
        if not node:
            return None 

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if not left and not right:
            return node 
        if not left:
            return node 

        if not right:
            node.right = left
            node.left = None 
            return node

        left_end = left
        while left_end.right:
            left_end = left_end.right

        right_end = right 
        while right_end.right:
            right_end = right_end.right

        left_end.right = right
        node.right = left
        node.left = None

        return node 





