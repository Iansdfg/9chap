"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        queue = deque([s])
        visited = set()
        step = 0 
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                visited.add(curr)
                if curr == t:
                    return step
                for node in curr.neighbors:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
            step += 1 
                        
        return -1
