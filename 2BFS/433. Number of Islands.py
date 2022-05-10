from collections import deque 
DIR = [(1, 0),(-1, 0),(0, 1),(0, -1)]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid):
        # write your code here
        isl = 0
        if not grid or not grid[0]:
            return isl
        visited = set()
        rows, cols = len(grid), len(grid[0]), 
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and (row, col) not in visited:
                    self.bfs(grid, row, col, visited)
                    isl += 1 
        return isl

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            curr_x, curr_y = queue.popleft()
            for delta_x, delta_y in DIR:
                next_x = curr_x + delta_x
                next_y = curr_y + delta_y
                if self.is_valid(grid, next_x, next_y, visited):
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
                
    def is_valid(self, grid, x, y, visited):
        rows, cols = len(grid), len(grid[0])
        
        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False 
        if (x, y) in visited:
            return False 

        return grid[x][y]
