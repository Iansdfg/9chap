"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        dummy = TreeNode(-1)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) != 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        curr = self.stack.pop()
        ans = curr
        if curr.right:
            curr = curr.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return ans 
        
        
        
        
