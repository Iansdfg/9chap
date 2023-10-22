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

class Solution:
    """
    @param preorder: A list of integers that preorder traversal of a tree
    @param inorder: A list of integers that inorder traversal of a tree
    @return: Root of a tree
    """
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # write your code here

        if preorder  == [] or inorder == []:
            return None 
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root_val = preorder[0]
        root_val_inorder_idx = inorder.index(preorder[0])

        left_len =  root_val_inorder_idx
        right_len = len(inorder) - root_val_inorder_idx

        left_inorder = inorder[:root_val_inorder_idx]
        left_preorder = preorder[1:1 + left_len]
        right_inorder = inorder[root_val_inorder_idx+1:]
        right_preorder = preorder[1 + left_len:]

        left_sub = self.build_tree(left_preorder, left_inorder)
        right_sub = self.build_tree(right_preorder, right_inorder)

        node = TreeNode(root_val)
        node.left = left_sub
        node.right = right_sub

        return node 


