from heapq import heapify, heappop, heappush
class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
                
        return heappop(heap)
            
