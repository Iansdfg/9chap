from collections import deque

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
        if root is None:
            return ""
        
        queue = deque([root])
        res = []
        while queue:
            curr_node = queue.popleft()
            res.append(str(curr_node.val) if curr_node else '#')
            if curr_node:
                queue.append(curr_node.left)
                queue.append(curr_node.right)
        return ' '.join(res)


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
        if not data:
            return None
    
        bfs_order = [    
            TreeNode(int(val)) if val != '#' else None
            for val in data.split()
        ]
        root = bfs_order[0]
        father_p, child_p = 0, 1
        nodes = [root]

        while father_p < len(nodes):
            node = nodes[father_p]
            father_p += 1 

            node.left = bfs_order[child_p]
            node.right = bfs_order[child_p + 1]
            child_p += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
                
        return root

