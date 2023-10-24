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
    @param root: a root of binary tree
    @return: return a integer
    """
    MAX = 0    
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        # write your code here
        h = self.dfs(root)
        return self.MAX

    def dfs(self, node: TreeNode):
        if not node:
            return 0

        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)

        self.MAX = max(self.MAX,left_height+right_height)

        return max(left_height, right_height) + 1

