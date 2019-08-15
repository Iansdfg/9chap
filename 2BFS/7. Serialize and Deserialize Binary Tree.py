"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


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
        queue = collections.deque([root])
        while queue:
            curr_node = queue.popleft()
            if not curr_node:
                data.append(None)
                continue
            data.append(curr_node)
            if curr_node.left:
                queue.append(curr_node.left)
            else:
                queue.append(None)
            if curr_node.right:
                queue.append(curr_node.right)
            else:
                queue.append(None)
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
        # for datum in data:
        #     print(datum.val if datum else None)
        # print('*******here*******')
        data_que = collections.deque(data)
        queue = collections.deque()
        root = data_que.popleft()
        queue.append(root)
        while queue:
            curr_node = queue.popleft()
            if curr_node:
                # print('curr_node',curr_node.val)
            
                nextt = data_que.popleft()
                # if nextt:
                    # print('nextt1',nextt.val)
                curr_node.left = nextt 
                queue.append(nextt)
                
                nextt = data_que.popleft()
                # if nextt:
                    # print('nextt2',nextt.val)
                curr_node.right = nextt 
                queue.append(nextt)
            
        return root
            
            
        
