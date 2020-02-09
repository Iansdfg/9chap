"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

from heapq import heappop, heappush

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
            dis = self.get_distance(point,origin)
            heappush(heap, (dis, point.x, point.y))
        
        res = []
        for i in range(k):
           res.append(heappop(heap)[1:]) 

        return res
            
    def get_distance(self, a, b):
        return (a.x - b.x)**2 + (a.y - b.y)**2
