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
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzag_level_order(self, root):
        # write your code here
        if not root:
            return []
        queue = deque([root])
        res = []
        flag = 0
        while queue:
            lv = []
            for i in range(len(queue)):
                curr = queue.popleft()
                lv.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if flag%2 == 0:
                res.append(lv)
            else:
                
                lv.reverse()
                res.append(lv)
            flag += 1 
        return res


