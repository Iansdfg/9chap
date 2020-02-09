from heapq import heappop, heappush, heappushpop

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.heap = []
        self.k = k 
        

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if self.k > len(self.heap):
            heappush(self.heap, num)
            
        elif self.k <= len(self.heap) and num > self.heap[0]:
            heappush(self.heap, num)
            heappop(self.heap)
            
    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        self.heap.sort()
        return self.heap[::-1]
