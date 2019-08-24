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
    def kthSmallest(self, root, k):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        
        for _ in range(k):
            curr_node = stack.pop()
            if curr_node.right:
                curr_node = curr_node.right
                while curr_node:
                    stack.append(curr_node)
                    curr_node = curr_node.left
                    
        return stack[-1].val
        
        
