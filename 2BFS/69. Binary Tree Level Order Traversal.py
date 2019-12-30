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
        if not root:return []
        
        queue = deque([root])
        result = [[root.val]]
        while queue:
            path = []
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    path.append(node.left.val)
                    queue.append(node.left)
                    
                if node.right:
                    path.append(node.right.val)
                    queue.append(node.right)
                    
            if path:
                result.append(path)
        return result
