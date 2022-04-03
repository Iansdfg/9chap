from lintcode import (
    ParentTreeNode,
)

""" 
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum3(self, root, target):
        # write your code here
        paths = []
        self.iterator(root, target, [], paths)
        return paths

    def iterator(self, root, target, path, paths):
        if not root:
            return
        print('root: ', root.val)
        # do dfs in every node. 
        self.dfs(root, target, root, path, paths)
        self.iterator(root.left, target, path, paths)
        self.iterator(root.right, target, path, paths)

    def dfs(self, root, target, prev, path, paths):
        path.append(root.val)
        print(path)
        if sum(path) == target:
            paths.append(path[:])

        for next_node in [root.parent, root.left, root.right]:
            if not next_node:
                continue
            if prev == next_node:
                continue
            self.dfs(next_node, target, root, path, paths)

        path.pop()

        

            
