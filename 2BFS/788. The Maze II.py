from collections import deque

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def shortestDistance(self, maze, start, destination):
        # write your code here
        queue = deque([[start[0], start[1], 0]])
        visited = set()
        
        result = float('inf')
        while queue:
            curr_x, curr_y, length = queue.popleft()
            visited.add((curr_x, curr_y))
            if [curr_x, curr_y] == destination:
                    result = min(length, result)
                    
            temp = length
            for delta_x, delta_y in self.directions:
                next_x = curr_x + delta_x
                next_y = curr_y + delta_y
                length += 1 
                
                while self.keep_rolling(maze, next_x, next_y):
                    next_x += delta_x
                    next_y += delta_y
                    length += 1 

                next_x -= delta_x
                next_y -= delta_y
                length -= 1
                
                if (next_x, next_y) not in visited:
                    queue.append([next_x, next_y, length])
                
                length = temp
                
        return -1 if result == float('inf') else result 
        

    def keep_rolling(self, maze, x, y):
        rows, cols = len(maze), len(maze[0])
        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False
        if maze[x][y] == 1:
            return False 
        return True
                
            
