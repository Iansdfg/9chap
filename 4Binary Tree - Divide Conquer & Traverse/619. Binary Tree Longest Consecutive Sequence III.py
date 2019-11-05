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
        max_len, _, _, = self.helper(root)
        return max_len
    
    def helper(self, root):
        if root is None:
            return 0, 0, 0

        max_len, up, down = 0, 0, 0
        for child in root.children:
            result = self.helper(child)
            max_len = max(max_len, result[0])
            if child.val + 1 == root.val:
                down = max(down, result[1] + 1)
            if child.val - 1 == root.val:
                up = max(up, result[2] + 1)

        max_len = max(down + 1 + up, max_len)

        return max_len, down, up
            
            
            
            
        
