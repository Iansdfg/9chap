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
        self.inorder(root, target, results)
        return results
            
    def inorder(self, root, target, results):
        if not root:
            return
        
        path = []
        self.dfs(root, None, target, path, results)
        
        self.inorder(root.left, target, results)
        self.inorder(root.right, target, results)

    def dfs(self, root, prev, target, path, results):
        path.append(root.val)
        
        if sum(path) == target:
            results.append(path[:])
        
        for neighber in [root.parent, root.left, root.right]:
            if not neighber or neighber == prev:
                continue
            self.dfs(neighber, root, target, path, results)
            
        
        path.pop()
        
        
            
            
            
            
            
