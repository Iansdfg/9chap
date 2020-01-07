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
            
        cols = len(grid[0])
        rows = len(grid)
        count = 0
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and (row, col) not in visited:
                    count += 1 
                    self.zeroify(grid, row, col, visited)
        return count
        
    def zeroify(self,grid, row, col, visited):
        queue = deque([(row, col)])
        visited.add((row, col))
        while queue:
            x, y = queue.popleft()
            grid[x][y] = 0
            for delta_x, delta_y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + delta_x, y + delta_y
                if not self.is_valid(grid, new_x, new_y, visited):
                    continue
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
        
    def is_valid(self, grid, x, y, visited):
        if (x, y) in visited:
            return False
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] == 0:
            return False
        return True
            
