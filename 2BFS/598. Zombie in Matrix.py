from collections import deque

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        rows, cols = len(grid), len(grid[0])
        human_num = 0
        zombie_list = []
        visited = set()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    human_num += 1 
                elif grid[row][col] == 1:
                    zombie_list.append((row, col))
                    
        queue = deque(zombie_list)
        count = 0
        day = 0
        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                visited.add((curr_x, curr_y))
                dirctions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for delta_x, delta_y in dirctions:
                    new_x, new_y = curr_x + delta_x, curr_y + delta_y
                    if self.is_valid(grid, new_x, new_y, visited):
                        count += 1
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
            day += 1 
        return day - 1 if count == human_num else -1
        
    def is_valid(self, grid, x, y, visited):
        if (x, y) in visited:
            return False 
        if x < 0 or x >= len(grid):
            return False
        if y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] != 0:
            return False 
        return True 
    
  
                 
