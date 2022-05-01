"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    max_val = 0
    def longestConsecutive3(self, root):
        # Write your code here
        self.dfs(root)
        return self.max_val

        
    def dfs(self, root):
        #return inc_len, dec_max
        if not root:
            return 0, 0
        
        if not root.children:
            return 1, 1

        max_inc_len = 0
        max_dec_len = 0

        is_incre = False
        is_decre = False
        for child in root.children:
            child_inc_len, child_dec_max = self.dfs(child)

            if child and child.val == root.val + 1:
                max_inc_len = max(max_inc_len, child_inc_len) 
                is_incre = True 

            if child and child.val == root.val - 1:
                max_dec_len = max(max_dec_len, child_dec_max) 
                is_decre = True 

        dec_len = max_dec_len + 1 if is_decre else 1 
        inc_len = max_inc_len + 1 if is_incre else 1 

        self.max_val = max(self.max_val, dec_len + inc_len - 1 )
        return inc_len, dec_len

