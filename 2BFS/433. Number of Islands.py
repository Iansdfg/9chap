import collections 

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.single_ify(grid, i, j, visited)
                    islands += 1
                    
        return islands          
        
        
    def single_ify(self,grid,row, col,visited):
        queue = collections.deque()
        queue.append((row, col))
        visited.add((row, col))
        while queue:
            x,y = queue.popleft()
            for delta_x,delta_y in [(0,1),(0,-1),(1,0),(-1,0)]:
                next_x = x+delta_x
                next_y = y+delta_y
                if not self.is_valid(grid, next_x, next_y,visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                
    def is_valid(self, grid, x, y,visited):
        n,m = len(grid),len(grid[0])
        return 0<=x<n and 0<=y<m and (x,y) not in visited and grid[x][y] 

