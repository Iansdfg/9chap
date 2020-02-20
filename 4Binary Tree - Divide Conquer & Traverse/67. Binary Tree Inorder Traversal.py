"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root
        stact = [dummy]
        in_order = []
        
        while stact:
            curr = stact.pop()
            if curr.right:
                curr = curr.right
                while curr:
                    stact.append(curr)
                    curr = curr.left
            if stact:
                in_order.append(stact[-1].val)
        return in_order
