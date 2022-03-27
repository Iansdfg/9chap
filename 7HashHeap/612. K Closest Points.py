from lintcode import (
    Point,
)
import heapq
"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points, origin, k):
        # write your code here
        heap = []
        for point in points:
            dist = self.get_distance(origin, point)
            heapq.heappush(heap, (dist, point.x, point.y))
        
        res = []
        for _ in range(k):
            dis, x, y  = heapq.heappop(heap)
            res.append(Point(x, y))
        return res 

    def get_distance(self, origin, point):
        x1, y1 = origin.x, origin.y
        x2, y2 = point.x, point.y
        return (x1 - x2)**2 + (y1 - y2)**2
