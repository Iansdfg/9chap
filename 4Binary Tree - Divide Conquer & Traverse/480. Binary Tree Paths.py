from typing import (
    List,
)
from lintcode import (
    TreeNode,
)
##########Bottom Up##########
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
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        # write your code here
        return self.dfs(root)

    def dfs(self, root):
        #return left path, right path 
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]
        
        left_path = self.dfs(root.left)
        right_path = self.dfs(root.right)
        
        new_path = []
        for path in left_path + right_path:
            new_path.append(str(root.val) + '->' + path)

        return new_path

        




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



from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

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
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        # write your code here
        res = []
        self.dfs(root, [], res)
        return res


    def dfs(self, node, path, res):
        if not node:
            return 

        if not node.left and not node.right:
            path.append(str(node.val))
            res.append('->'.join(path[:]))
            path.pop()
            return 

        for node_ in [node.left, node.right]:
            path.append(str(node.val))
            self.dfs(node_, path, res)
            path.pop()




       
