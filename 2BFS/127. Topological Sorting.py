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
        if not graph:
            return []
        node_indegree = self.get_indegree(graph)
        starts = [key for key in node_indegree if node_indegree[key] == 0]
        queue = deque(starts)
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbor in curr.neighbors:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order
                
     

    def get_indegree(self, graph):
        node_indegree = {x:0 for x in graph }
        for node in graph:
            for neighbor in node.neighbors:
                node_indegree[neighbor] += 1 
        return node_indegree


########################10/4/2022########################
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

        node_to_indegree = dict()
        for node in graph:
            node_to_indegree[node] = 0

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1 

        queue = deque([])
        for node in node_to_indegree:
            # print(key.label, node_to_indegree[key])
            if node_to_indegree[node] == 0:
                queue.append(node)

        topOrde = []
        while queue:
            curr = queue.popleft()
            topOrde.append(curr)

            for neighbor in curr.neighbors:
                node_to_indegree[neighbor] -= 1 
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)

        return topOrde


        

