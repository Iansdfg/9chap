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
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root, target):
        # write your code here
        paths = []
        self.dfs(root, target, [], paths)
        return paths

    def dfs(self, root, target, path, paths):
        if not root:
            return 

        path.append(root.val)
        if not root.left and not root.right and sum(path) == target:
            paths.append(path[:])
      
        self.dfs(root.left, target, path, paths)
        self.dfs(root.right, target, path, paths)
        path.pop()
