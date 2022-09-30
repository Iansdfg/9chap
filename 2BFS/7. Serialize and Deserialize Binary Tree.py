"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        queue = deque([root])
        res = []

        while queue:
            curr = queue.popleft()
            if curr:
                res.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append('#')
        # convert to string is a more store effeficent way 
        return res

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        print(data)
        nodes = []
        for datum in data:
            if datum == '#':
                nodes.append(None)
            else:
                nodes.append(TreeNode(datum))
        
        #a-ha point: every loop father incrment by 1 child increment by 2 
        root = nodes[0]
        father_p, child_p = 0, 1
        while child_p < len(data):
            if nodes[father_p]:
                nodes[father_p].left = nodes[child_p]
                nodes[father_p].right = nodes[child_p + 1]
                child_p += 2
            father_p += 1

        return root
            



