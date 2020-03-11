from collections import deque

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    derictions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def hasPath(self, maze, start, destination):
        # write your code here
        queue = deque([start])
        visited = set()
        
        while queue:
            curr_x, curr_y = queue.popleft()
            print(curr_x, curr_y)
            visited.add((curr_x, curr_y))
            if [curr_x, curr_y] == destination:
                    return True
                    
            for delta_x, delta_y in self.derictions:
                next_x, next_y = curr_x + delta_x, curr_y + delta_y
                
                while self.keep_rolling(maze, next_x, next_y):
                    next_x, next_y = next_x + delta_x, next_y + delta_y

                next_x, next_y = next_x - delta_x, next_y - delta_y
                
                if (next_x, next_y) not in visited:
                    queue.append((next_x, next_y))
                
        return False 
                
    def keep_rolling(self, maze, x, y):
        rows, cols = len(maze), len(maze[0])
        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False
        if maze[x][y] == 1:
            return False 
        return True
                
            
