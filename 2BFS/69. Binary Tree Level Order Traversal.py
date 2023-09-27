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
import collections

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue: 
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level)
        return res 

        
