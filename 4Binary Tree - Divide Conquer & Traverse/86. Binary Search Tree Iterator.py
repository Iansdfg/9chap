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
        self._next()

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        if self.stack:
            return True
        return False

    """
    @return: return next node
    """
    def _next(self):
        # write your code here
        curr = self.stack.pop()
        res = curr
        if curr.right:
            curr = curr.right
            self.stack.append(curr)
            while curr.left:
                curr = curr.left
                self.stack.append(curr)
        return res 
        


        
##############################10/25/2022##############################
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
        self._next()

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.stack) != 0

    """
    @return: return next node
    """
    def _next(self):
        # write your code here
        curr = self.stack.pop()
        res = curr
        if curr.right:
            curr = curr.right
            self.stack.append(curr)
            while curr.left:
                curr = curr.left
                self.stack.append(curr)

        return res


            



