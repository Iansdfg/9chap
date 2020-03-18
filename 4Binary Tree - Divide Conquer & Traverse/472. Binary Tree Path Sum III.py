"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        results = []
        self.helper(root, target, results)
        return results
        
        
    def helper(self, root, target, results):
        if not root:
            return 
        
        self.dfs(root, target, None, [], results)
        
        self.helper(root.left, target, results)
        self.helper(root.right, target, results)
        
    def dfs(self, root, target, prev, path, results):
        path.append(root.val)
     
        if sum(path) == target:
            print(path)
            results.append(path[:])
            
        for next_node in [root.parent, root.left, root.right]:
            if not next_node:
                continue
            if next_node == prev:
                continue
            self.dfs(next_node, target, root, path, results)
        
        path.pop()
