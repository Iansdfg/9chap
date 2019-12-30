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
        data = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            if not node:
                data.append(None)
                continue
            data.append(node)
            
            queue.append(node.left if node.left else None)
            queue.append(node.right if node.right else None)

        return data
            

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
        data_queue = deque(data)
        root = data_queue.popleft()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                
                nextt = data_queue.popleft()
                node.left = nextt
                queue.append(nextt)
                
                nextt = data_queue.popleft()
                node.right = nextt
                queue.append(nextt)
                
        return root 
                
