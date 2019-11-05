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
        result = []
        self.dfs(root, target, result)
        return result
        
    def dfs(self, root, target, result):
        if not root:
            return 
        path = []
        
        self.path_sum(root, target, path, result, None)
        
        self.dfs(root.left, target, result)
        self.dfs(root.right, target, result)
        
        
    def path_sum(self, root, target, path, result, father):
        if not root:
            return
        path.append(root.val)
        target -= root.val
        
        if target == 0:
            result.append(path[:])
            
        if root.parent and root.parent != father:
            self.path_sum(root.parent, target, path, result, root)
            
        if root.left and root.left != father:
            self.path_sum(root.left, target, path, result, root)
            
        if root.right and root.right != father:
            self.path_sum(root.right, target, path, result, root)
            
        path.pop()
            
