"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        queue = deque([(source.x, source.y)])
        visited = set()
        count = 0
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == destination.x and y == destination.y:
                    return count
                
                for delta_x, delta_y in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]:
                    next_x, next_y = x + delta_x, y + delta_y
                    if self.is_valid(grid, next_x, next_y, visited):
                        queue.append((next_x, next_y))
                        visited.add((next_x, next_y))
            count += 1 
        return -1
        
    def is_valid(self,grid, x, y, visited):
        rows, cols = len(grid), len(grid[0])
        if (x, y) in visited:
            return False
        if x < 0 or x >= rows:
            return False
        if y < 0 or y >= cols:
            return False
        if grid[x][y] == 1:
            return False
        return True





