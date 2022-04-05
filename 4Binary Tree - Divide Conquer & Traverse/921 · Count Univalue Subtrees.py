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
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """

    def count_unival_subtrees(self, root):
        # write your code here
        is_unival, total_num = self.dfs(root)
        return total_num

    def dfs(self, root):
        #return is_unival, num of unival,val 
        if not root:
            return True, 0
        if not root.left and not root.right:
            return True, 1

        left_is_unival, left_num = self.dfs(root.left)
        right_is_unival, right_num = self.dfs(root.right)

        total_num = right_num + left_num

        if root.left and root.right:
            is_unival = root.val == root.left.val and root.val == root.right.val and  left_is_unival and right_is_unival
        elif root.left:
            is_unival = root.val == root.left.val and left_is_unival
        elif root.right:
            is_unival = root.val == root.right.val and right_is_unival

        if is_unival == True:
            total_num += 1 
        return is_unival, total_num
        
 
