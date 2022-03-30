import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        res = []
        for num in nums:
            heapq.heappush(res, num)
            if len(res) > k:
                heapq.heappop(res)
        res.sort()
        res.reverse()
        return res


        
