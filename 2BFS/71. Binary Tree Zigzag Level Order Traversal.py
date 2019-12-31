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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here

        if not root:
            return []
        queue = deque([root])
        result = [[root.val]]
        count = 1
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
                if count%2:
                    result.append(path[::-1])
                else:
                    result.append(path)
                count += 1
                        
        return result
