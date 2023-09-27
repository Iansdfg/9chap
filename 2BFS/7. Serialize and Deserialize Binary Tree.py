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
        index_node = {}
        for index, value in enumerate(data):
            if value != '#':
                index_node[index+1] = TreeNode(value)
            else:
                index_node[index+1] = None
        
        slow_p, fast_p = 1, 2
        while fast_p < len(data):
            if not index_node[slow_p]:
                slow_p += 1
            else:
                index_node[slow_p].left = index_node[fast_p]
                index_node[slow_p].right = index_node[fast_p + 1]
                slow_p += 1 
                fast_p += 2 

        return index_node[1]

        



