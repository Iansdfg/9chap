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
from collections import deque
class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def right_side_view(self, root: TreeNode) -> List[int]:
        # write your code here
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            lv = []
            for i in range(len(queue)):
                curr = queue.popleft()
                lv.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(lv[-1])
        return res 
            




