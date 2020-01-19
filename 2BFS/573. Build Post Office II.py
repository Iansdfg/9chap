from collections import deque
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        rows, cols = len(grid), len(grid[0])
        result = float('inf')
        house_num = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    house_num += 1
                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    dist = self.bfs(grid, row, col, house_num)
                    result = min(dist, result)
                    
        return result
        
    def bfs(self, grid, x, y, house_num):
        queue = deque([(x, y)])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        distance = 0
        total_dist = 0
        house_count = 0
        
        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                visited.add((curr_x, curr_y))
                if grid[curr_x][curr_y] == 1:
                    house_count += 1
                    total_dist += distance
                for delta_x, delta_y in direction:
                    next_x, next_y = curr_x + delta_x, curr_y + delta_y
                    if self.is_valid(grid, next_x, next_y, visited):
                        queue.append((next_x, next_y))
                        visited.add((next_x, next_y))
            distance += 1 
            
        return total_dist if house_count == house_num else -1
            
    def is_valid(self, grid, x, y, visited):
        if (x, y) in visited:
            return False 
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] == 2:
            return False 
        return True
        
            
            
            
            
                    
                
            
            
        
        
