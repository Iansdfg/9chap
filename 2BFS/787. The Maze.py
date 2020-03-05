from collections import deque
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    def hasPath(self, maze, start, destination):
        # write your code here
        queue = deque([start])
        visited = set((start[0], start[1]))
        while queue:
            curr_x, curr_y = queue.popleft()
            visited.add((curr_x, curr_y))
            if [curr_x, curr_y] == destination:
                return True
                
            for delta_x, delta_y in self.directions:
                next_x, next_y = curr_x + delta_x, curr_y + delta_y
                
                while self.keep_rolling(maze, next_x, next_y):
                    next_x += delta_x
                    next_y += delta_y
                # at this time maze[x][y] == 1 so go back
                next_x -= delta_x
                next_y -= delta_y
                    
                if self.is_valid(maze, next_x, next_y, visited):
                    queue.append([next_x, next_y])
            
        return False
        
    def keep_rolling(self, maze, x, y):
        rows = len(maze)
        cols = len(maze[0])
        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False 
        if maze[x][y] == 1:
            return False
        return True
        
    def is_valid(self, maze, x, y, visited):
        rows = len(maze)
        cols = len(maze[0])
        
        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False 
        if maze[x][y] == 1:
            return False
        if (x, y) in visited:
            return False
        return True
