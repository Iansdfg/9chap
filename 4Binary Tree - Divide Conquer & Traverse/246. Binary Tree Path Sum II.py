"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        results = []
        self.dfs(root, target, [], results)
        return results
        
    def dfs(self, root, target, path, results):
        if not root:
            return
        
        path.append(root.val)
        for i in range(len(path)):
            if sum(path[i:]) == target:
                results.append(path[i:])
            
        self.dfs(root.left, target, path, results)
        self.dfs(root.right, target, path, results)
        path.pop()
