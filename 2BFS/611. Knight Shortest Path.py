# """
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
# """
# DIRECTIONS = [
#     (-2, -1), (-2, 1), (-1, 2), (1, 2),
#     (2, 1), (2, -1), (1, -2), (-1, -2),
# ]
# class Solution:
#     """
#     @param grid: a chessboard included 0 (false) and 1 (true)
#     @param source: a point
#     @param destination: a point
#     @return: the shortest path 
#     """
#     def shortestPath(self, grid, source, destination):
#         # write your code here
#         if not grid or not grid[0]: return -1
#         queue = collections.deque([(source.x,source.y)])
#         distance = {(source.x,source.y):0}
        
#         while queue:
#             curr_x, curr_y = queue.popleft()
#             if (curr_x, curr_y) == (destination.x, destination.y):
#                     return distance[(curr_x, curr_y)]
#             for delta_x, delta_y in DIRECTIONS:
#                 next_x = curr_x + delta_x
#                 next_y = curr_y + delta_y
#                 if (next_x, next_y) in distance or not self.is_valid(next_x, next_y,grid):
#                     continue
#                 distance[(next_x, next_y)] = distance[(curr_x, curr_y)]+1
#                 queue.append((next_x, next_y))
#         return -1  
    
#     def is_valid(self, x, y, grid):
#         m, n = len(grid), len(grid[0])
#         return 0 <= x < m and 0 <= y < n and not grid[x][y]
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        
        if not grid or not grid[0]: return -1
        queue = collections.deque()
        queue.append((source.x,source.y))
        visited = set()
        visited.add((source.x,source.y))
        level = 1
        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                directions = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
                for delta_x, delta_y in directions:
                    new_x = curr_x + delta_x
                    new_y = curr_y + delta_y
                    if (new_x, new_y) == (destination.x, destination.y):
                        return level
                    if self.is_valid(new_x, new_y, grid, visited):
                        queue.append((new_x,new_y))
                        visited.add((new_x,new_y))
            level+=1
        return -1
    
    def is_valid(self, x, y, grid, visited):
        m, n = len(grid), len(grid[0])
        return 0 <= x < m and 0 <= y < n and not grid[x][y] and (x, y) not in visited
