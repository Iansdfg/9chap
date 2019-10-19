import heapq

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

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
            dis = self.get_dis(point, origin)
            heapq.heappush(heap, (-dis, -point.x, -point.y))
            if len(heap)>k:
                heapq.heappop(heap)
                
        result = []
        while len(heap)>0:
            dis, x, y = heapq.heappop(heap)
            result.append((-x,-y))
            
            
        result.reverse()
        return result
            
    def get_dis(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
        
