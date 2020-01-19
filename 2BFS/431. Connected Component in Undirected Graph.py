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
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        visited = set()
        components = []
        for node in nodes:
            if node in visited:
                continue
            component = self.bfs(nodes, node, visited)
            components.append(sorted(component))
        return components
        
        
    def bfs(self, nodes, node, visited):
        queue = deque([node])
        result = []
        
        while queue:
            curr = queue.popleft()
            result.append(curr.label)
            visited.add(curr)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
                
        
        
        
            
                
