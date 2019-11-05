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
    def longestConsecutive3(self, root):
        # Write your code here
        max_len, _, _ = self.helper(root)
        return max_len
        
    def helper(self, root):
        # max_len, up, down
        if not root:
            return 0, 0, 0
        
        length, up, down = 0, 0, 0
        for child in root.children:
            child_len, child_up, child_down = self.helper(child)
            length = max(length, child_len)
            if child.val == root.val - 1:
                down = max(down, child_down + 1)
            if child.val == root.val + 1:
                up = max(up, child_up + 1)
        
        length = max(length, down + up + 1)

        
        return length, up, down
            
        
        
