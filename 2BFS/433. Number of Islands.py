from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if grid == [] or grid[0] == []:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        visited = set()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    island += 1
                    visited.add((row, col))
                    self.bfs(grid, row, col, visited)
        return island
        
    
    def bfs(self, grid, row, col, visited):
        queue = deque([(row, col)])
        while queue:
            x,y = queue.popleft()
            grid[x][y] = 0
            for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + delta_x, y + delta_y
                if self.is_valid(grid,new_x, new_y,visited):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
    
                    
    def is_valid(self, grid, x, y, visited):
        rows = len(grid)
        cols = len(grid[0])
        if (x, y) in visited:
            return False
        if x < 0 or x >= rows:
            return False
        if y < 0 or y >= cols:
            return False
        return grid[x][y] == 1 
        
     
