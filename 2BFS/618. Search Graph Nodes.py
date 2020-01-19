"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        if not graph:
            return False 
            
        if values[node] == target:
            return node 
        
        node_to_level = {}
        
        queue = deque([node])
        visited = set()
        level = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                visited.add(curr)
                for neighbor in curr.neighbors:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append(neighbor)
                    if values[neighbor] == target:
                        node_to_level[neighbor] = level
            level += 1
            
        if not node_to_level:
            return None 
            
        for node in node_to_level:
            if node_to_level[node] == min(node_to_level.values()):
                return node

    
        
        
