"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
from collections import deque
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    
    def topSort(self, graph):
        # write your code here
        node_indegree = {}

        for node in graph:
            if node not in node_indegree:
                node_indegree[node] = 0

            for neighbor in node.neighbors:
                if neighbor in node_indegree:
                    node_indegree[neighbor]+=1
                else:
                    node_indegree[neighbor] = 1
        
        queue = deque([])
        for node in node_indegree:
            if node_indegree[node] == 0:
                queue.append(node)

        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for neighbor in curr.neighbors:
                node_indegree[neighbor] -= 1 
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return res




        
        
