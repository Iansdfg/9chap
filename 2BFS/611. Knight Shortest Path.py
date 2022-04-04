##############dict() store steps ##############
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""
DIR = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1),]
from collections import deque 
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid, source, destination):
        # write your code here
        queue = deque([(source.x, source.y)])
        p_to_dist = {(source.x, source.y):0}

        while queue:
            curr_x, curr_y = queue.popleft()
            if (curr_x, curr_y) == (destination.x, destination.y):
                return p_to_dist[(curr_x, curr_y)]
            for delta_x, delta_y in DIR:
                next_x = delta_x + curr_x
                next_y = delta_y + curr_y
                if (next_x, next_y) in p_to_dist:
                    continue
                if not self.is_valid(grid, next_x, next_y):
                    continue
                p_to_dist[(next_x, next_y)] = p_to_dist[(curr_x, curr_y)] + 1 
                queue.append((next_x, next_y))
        
        return -1 

    def is_valid(self, grid, x, y):
        rows, cols = len(grid), len(grid[0])
        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False 
        if grid[x][y] == 1: 
            return False 
        return True 

    
    
##############分层##############
from lintcode import (
    Point,
)
DIRECTIONS = [
    (1, 2), (1, -2), (-1, 2), (-1, -2),
    (2, 1), (2, -1), (-2, 1), (-2, -1),
]
"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid, source, destination):
        # write your code here

        queue = deque([(source.x, source.y)])
        visited = set()
        step = 0
        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()

                if (curr_x, curr_y) == (destination.x, destination.y):
                    return step
                visited.add((curr_x, curr_y))
                
                for delta_x, delta_y in DIRECTIONS:
                    next_x = curr_x + delta_x
                    next_y = curr_y + delta_y

                    if self.is_valid(grid, next_x, next_y, visited):
                        queue.append((next_x, next_y))
            step += 1 

        return -1

    def is_valid(self, grid, x, y, visited):
        rows = len(grid)
        cols = len(grid[0])

        if x < 0 or x >= rows:
            return False 
        if y < 0 or y >= cols:
            return False 
        if (x, y) in visited:
            return False
        return grid[x][y] != 1
        
            





        

