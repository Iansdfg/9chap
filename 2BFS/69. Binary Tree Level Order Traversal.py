"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        queue = deque([root])
        result = []
        while queue:
            path = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                
                path.append(node.val)
                queue.append(node.left if node.left else None)
                queue.append(node.right if node.right else None)
            
            if path:
                result.append(path)
                
        return result
                
                
