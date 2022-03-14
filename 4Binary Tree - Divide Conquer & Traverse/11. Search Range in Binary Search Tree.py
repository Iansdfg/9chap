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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root, k1, k2):
        # write your code here
        if not root:
            return[]

        queue = deque([root])
        res = []
        while queue:
            curr = queue.popleft()
            if k1 <= curr.val <= k2:
                res.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return sorted(res)
    
    
    
    
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root, k1, k2):
        # write your code here
        res = []
        self.inorder(root, k1, k2, res)
        return sorted(res)

    def inorder(self, root, k1, k2, res):
        if not root:
            return

        if root.val > k1:
            self.inorder(root.left, k1, k2, res)
        if root.val < k2:
            self.inorder(root.right, k1, k2, res)
        if k1 <= root.val <= k2:
            res.append(root.val) 
