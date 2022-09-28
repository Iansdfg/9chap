from typing import (
    List,
)
from collections import deque
Directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0
        num_island = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and (row, col) not in visited:
                    self.bfs(row, col, grid, visited)
                    num_island += 1 

        return num_island


    def bfs(self, x, y, grid, visited):
        queue = deque([(x,y)])
        visited.add((x, y))

        while queue:
            curr_x, curr_y = queue.popleft()
            for delta_x, delta_y in Directions:
                next_x, next_y = curr_x + delta_x, curr_y + delta_y
                if not self.is_valid(next_x, next_y, grid, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))


    def is_valid(self, x, y, grid, visited):
        rows = len(grid)
        cols = len(grid[0])
        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False 
        if (x,y) in visited:
            return False 
        return grid[x][y] 






