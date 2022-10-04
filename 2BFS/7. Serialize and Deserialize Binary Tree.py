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
        res = ''
        while queue:
            curr = queue.popleft()
            
            if curr:
                res += str(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res += '#'
            if queue:
                res += ','
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
        data_list = data.split(',')
        node_list = []
        for datum in data_list:
            if datum == '#':
                node_list.append(None)
            else:
                node_list.append(TreeNode(int(datum)))
        
        father_p, child_p = 0, 1

        while child_p < len(node_list):
            if node_list[father_p]:
                node_list[father_p].left = node_list[child_p]
                node_list[father_p].right = node_list[child_p + 1]
                child_p += 2
            father_p += 1 
  

        return node_list[0]

           
