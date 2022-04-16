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
    @param root: the root
    @return: the largest subtree's size which is a Binary Search Tree
    """
    max_node = [] 
    max_num = float('-inf')

    def largest_b_s_t_subtree(self, root):
        # Write your code here
        _, max_num = self.dfs(root)
        print(self.max_node)
        return max_num


    def dfs(self, root):
        #return is_bst, num, node 
        if not root:
            return True, 0 

        left_is_bst, left_num = self.dfs(root.left)
        right_is_bst, right_num = self.dfs(root.right)

        is_bst = self.isValidBST(root) and left_is_bst and right_is_bst

        if is_bst:
            num = left_num + right_num + 1 
        else:
            num = max(left_num, right_num)

        return is_bst, num

    
    def isValidBST(self, root):
        # write your code here
        max_num, min_num, is_bst = self.is_bst(root)
        return is_bst


    def is_bst(self, root):
        #Return max_num, min_num, is_bst 
        if not root:
            return float('-inf'), float('inf'), True, 
        
        left_max, left_min, left_is_bst = self.is_bst(root.left)
        right_max, right_min, right_is_bst = self.is_bst(root.right)

        is_bst = left_is_bst and right_is_bst and left_max < root.val  and root.val < right_min 

        max_num = max(root.val, left_max, right_max)
        min_num = min(root.val, left_min, right_min)

        return max_num, min_num, is_bst

