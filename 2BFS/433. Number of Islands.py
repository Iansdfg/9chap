class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]: return 0
        num_island = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and (row, col) not in visited:
                    self.bfs(row, col, grid, visited)
                    num_island+=1
        return num_island
        
    def bfs(self, x, y, grid, visited):
        queue = collections.deque()
        queue.append((x,y))
        visited.add((x, y))
        while queue:
            curr_x, curr_y = queue.popleft()
            # visited.add((curr_x, curr_y))
            for delta_x, delta_y in [(1,0),(-1,0),(0,1),(0,-1)]:
                alter_x = curr_x + delta_x
                alter_y = curr_y + delta_y
                if not self.is_valid(alter_x, alter_y, grid, visited):
                    continue
                queue.append((alter_x, alter_y))
                visited.add((alter_x, alter_y))
                    
                
    def is_valid(self, x, y, grid,visited):
        m,n = len(grid), len(grid[0])
        return  0<=x<m and 0<=y<n and grid[x][y] and (x,y) not in visited
                
     
