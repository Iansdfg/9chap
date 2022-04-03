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
        paths = []
        self.path_sum(root, target, [], paths)
        return paths

    def path_sum(self, root, target, path, paths):
        #return lefypath and sum
        if not root:
            return 

        path.append(root.val)
        temp = target
        for i in range(len(path)):
            if sum(path[i:]) == target:
                paths.append(path[i:]) 


        self.path_sum(root.left, target, path, paths)
        self.path_sum(root.right, target, path, paths)
        path.pop()

