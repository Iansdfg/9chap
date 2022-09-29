from typing import (
    List,
)
from collections import deque
Directions = [(0, 1),(1, 0),(0, -1),(-1, 0)]
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        isls = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue
                if grid[row][col]:
                    isls += 1
                    self.bfs(grid, row, col, visited)
        return isls

    #在哪里标记visited
    #1:add 一次 但复杂度高
    #2:add 两次 但复杂度低 提前check, 避免重复
    def bfs(self, grid, row, col, visited):
        queue = deque([(row, col)])
        #2
        visited.add((row, col))

        while queue:
            curr_x, curr_y = queue.popleft()
            #1
            # visited.add((curr_x, curr_y))
            # print(1)
            for delta_x, delta_y in Directions:
                next_x = delta_x + curr_x
                next_y = delta_y + curr_y
                if self.is_valid(grid, next_x, next_y, visited):
                    queue.append((next_x, next_y))
                    #2
                    visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        if x < 0 or x >= len(grid):
            return False 
        if y < 0 or y >= len(grid[0]):
            return False 
        if (x, y) in visited:
            return False 
        return grid[x][y]

