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
    def binary_tree_path_sum2(self, root, target):
        # write your code here
        result = []
        self.dfs(root, target, [], result)
        return result


    def dfs(self, root, target, path, result):
        if not root:
            return
        
        path.append(root.val)
        
        for i in range(len(path)):
            if sum(path[i:]) == target:
                result.append(path[i:])

        for next_node in [root.left, root.right]:
            self.dfs(next_node, target, path, result)
        path.pop()

