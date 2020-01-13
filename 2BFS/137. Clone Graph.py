"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

from collections import deque

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node
            
        nodes = self.get_nodes(node)
        old_to_new = {}
    
        for old_node in nodes:
            new_node = UndirectedGraphNode(old_node.label)
            old_to_new[old_node] = new_node
        # print(old_to_new)
            
        for old_node in nodes:
            new_node = old_to_new[old_node]
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(old_to_new[neighbor])
                
        return old_to_new[node]
            
    def get_nodes(self, node):
        queue = deque([node])
        nodes = set()
        
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor in nodes:
                    continue
                queue.append(neighbor)
            nodes.add(node)
        return nodes
        
