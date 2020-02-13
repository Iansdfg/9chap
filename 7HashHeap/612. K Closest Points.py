"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from heapq import heappush, heappop

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        
        heap = []
        for point in points:
            dis = self.distance(point, origin)
            heappush(heap, (dis, point.x, point.y))
        res = []
        for _ in range(k):
            dis, point_x, point_y = heappop(heap)
            res.append(Point(point_x, point_y))
        return res
            
    
    def distance(self, A, B):
        return (A.x - B.x)**2 + (A.y - B.y)**2
