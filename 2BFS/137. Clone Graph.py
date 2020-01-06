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
    def get_node(self, node):
        result = set()
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in result:
                    queue.append(neighbor)
            result.add(node)
        return result
            
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node
        old_nodes = self.get_node(node)
        
        old_to_new = dict()
        for old_node in old_nodes:
            old_to_new[old_node] = UndirectedGraphNode(old_node.label)
            
        for old_node in old_nodes:
            new_node = old_to_new[old_node]
            for neighbor in old_node.neighbors:
                new_neighbor = old_to_new[neighbor]
                new_node.neighbors.append(new_neighbor)
                
        return old_to_new[node]
            
    
    
    
    
    
    
    
    
            
            
            
            
            
            
            
