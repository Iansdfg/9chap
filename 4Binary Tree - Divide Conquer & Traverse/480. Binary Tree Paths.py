"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        results = []
        self.dfs(root, [], results)
        return results
        
        
    def dfs(self, root, path, results):
        if not root:
            return
        
    
        path.append(str(root.val))
        if not root.left and not root.right:
            results.append( '->'.join(path[:]))

        self.dfs(root.left, path, results)
        self.dfs(root.right, path, results)
        path.pop()
        
       
