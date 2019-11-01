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
        result = []
        self.dfs(root, target, [], result, 0, 0)
        return result
        
    def dfs(self, root, target, path, result, summ, level):
        if not root:
            return 
        
        path.append(root.val)
        summ += root.val

        for i in range(len(path)):
            if sum(path[i:]) == target:
                result.append(path[i:])
        
        self.dfs(root.left, target, path, result, summ, level)
        self.dfs(root.right, target, path, result, summ, level)
        
        summ -= root.val
        path.pop()
