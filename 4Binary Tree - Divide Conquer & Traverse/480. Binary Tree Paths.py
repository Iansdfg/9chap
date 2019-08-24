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
        if not root: return []
        
        res = []
        self.find_path(root, res, [str(root.val)])
        
        return res 
    
    def find_path(self, root, res, path):
        if not root.left and not root.right:
            res.append("->".join(path))
            return
            
        if root.left:
            path.append(str(root.left.val))
            self.find_path(root.left, res,path )
            path.pop()
            
        if root.right:
            path.append(str(root.right.val))
            self.find_path(root.right, res,path )
            path.pop()
