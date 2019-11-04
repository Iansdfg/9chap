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
        self.find_sum(root, target, None, path, result)
        
        self.dfs(root.left, target, result)
        self.dfs(root.right, target, result)
        
    def find_sum(self, root, target, father, path, result):
        
        path.append(root.val)
        target -= root.val
        
        if target == 0: 
            result.append(path[:])
            
        if root.parent not in [None, father]:
            self.find_sum(root.parent, target, root, path, result)
            
        if root.left not in [None, father]:
            self.find_sum(root.left, target, root, path, result)
            
        if root.right not in [None, father]:
            self.find_sum(root.right, target, root, path, result)
    
        
        path.pop()
        
