from collections import deque, defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        # valid tree: n-1 == len(edges) and all nodes can be visited 
        if n-1 != len(edges):
            return False
            
        node_to_neighbers = defaultdict(list)
        for x,y in edges:
            node_to_neighbers[x].append(y)
            node_to_neighbers[y].append(x)
            
        visited = set()
        queue = deque([0])
        
        while queue:
            curr = queue.popleft()
            if curr not in visited:
                visited.add(curr)
            visited.add(curr)
            for neighber in node_to_neighbers[curr]:
                if neighber not in visited:
                    visited.add(neighber)
                    queue.append(neighber)
                
        return len(visited) == n
                
