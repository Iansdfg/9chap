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
    def binaryTreePathSum(self, root, target):
        # write your code here
        results = []
        self.dfs(root, target, [], results)
        return results
        
    def dfs(self, root, target, path, results):
        if not root:
            return 
        
        path.append(root.val)
        
        if not root.left and not root.right and target == root.val:
            results.append(path[:])

        self.dfs(root.left, target-root.val, path, results)
        self.dfs(root.right, target-root.val, path, results)
        path.pop()
        
        
 
 
