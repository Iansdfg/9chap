from collections import deque
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n, edges):
        # write your code here

        if len(edges) != n-1:
            return False

        node_to_neighbers = {x:[] for x in range(n)}
        visited = set()

        for edge in edges:
            v1, v2 = edge[0], edge[1]
            node_to_neighbers[v1].append(v2)
            node_to_neighbers[v2].append(v1)

        print(node_to_neighbers)

        queue = deque([0])

        while queue:
            curr = queue.popleft()
            visited.add(curr)
            for neighber in node_to_neighbers[curr]:
                if neighber in visited:
                    continue
                queue.append(neighber)

        return len(visited) == n 


        

        

        

        
