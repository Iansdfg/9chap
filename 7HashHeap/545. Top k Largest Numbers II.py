import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.heap = []
        heapq.heapify(self.heap)
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        heapq.heappush(self.heap, num)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)

    """
    @return: Top k element
    """
    def topk(self):
        self.heap.sort()
        return self.heap[::-1]

