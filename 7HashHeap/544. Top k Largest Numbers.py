from heapq import heappush, heappop
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        heap = [] 
        for num in nums:
            heappush(heap, num)
            if len(heap)>k:
               heappop(heap)
               
        heap.sort()
        heap.reverse()
        return heap 
