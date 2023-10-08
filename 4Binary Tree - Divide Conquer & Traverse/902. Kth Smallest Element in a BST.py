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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        # write your code here
        if not root:
            return None 
        dummy = TreeNode(-1)
        dummy.right = root
        stack = [dummy]
        res = None 

        for _ in range(k+1):
            curr = stack.pop()
            res = curr.val 

            if curr.right:
                curr = curr.right
                stack.append(curr)
                # while 在 if loop 中 因为 left child is already put into stack
                while curr.left:
                    curr = curr.left
                    stack.append(curr)

        return res
