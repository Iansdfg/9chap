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
        self.dfs(root, target, 0, [], results)
        return results

        
    def dfs(self, root, target, level, path, results):
        if not root:
            return
        
        path.append(root.val)
        
        print(path)
        
        cur_sum = 0
        for i in range(level,-1, -1):
            cur_sum += path[i]
            # print(path, cur_sum)
            if cur_sum == target:
                results.append(path[i:])
                
        self.dfs(root.left, target, level + 1, path, results)
        self.dfs(root.right, target, level + 1, path, results)
        
        path.pop()
        
 
            
            
            
            
            
            
            
            

        
