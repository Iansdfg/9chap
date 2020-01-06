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
        if not root:
            return []
        queue = deque([root])
        result = [[root.val]]
        while queue:
            path = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    path.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    path.append(curr.right.val)
            if path:
                result.append(path)
        return result
                    
