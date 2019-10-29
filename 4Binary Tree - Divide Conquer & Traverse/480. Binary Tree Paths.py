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
        if not root:
            return []
        result = []
        self.dfs(root, [], result)
        return result
        
    def dfs(self, root, path, result):
        if not root:
            return 
        
        path.append(str(root.val))
        if not root.left and not root.right:
            ans = '->'.join(path)
            result.append(ans)

        self.dfs(root.left, path, result)
        self.dfs(root.right, path, result)
        path.pop()
        
      
