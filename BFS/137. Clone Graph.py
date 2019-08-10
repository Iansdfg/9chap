"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if node == None:return None
        visited = [node]
        queue = collections.deque()
        queue.append(node)
        node_dic = dict()
        node_dic[node] = UndirectedGraphNode(node.label)
        node_dic[node].neighbors=[]
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors :
                if neighbor not in visited:
                    copy_node = UndirectedGraphNode(neighbor.label)
                    copy_node.neighbors = []
                    node_dic[neighbor] = copy_node
                    visited.append(neighbor)
                    queue.append(neighbor)
        for dic_key_node in node_dic:
            for neighbor in dic_key_node.neighbors:
                node_dic[dic_key_node].neighbors.append(node_dic[neighbor])
    
        return node_dic[node]
