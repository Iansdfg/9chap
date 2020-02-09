import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        visited = set([1])
        
        val = None 
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_num = factor * val 
                if new_num not in visited:
                    visited.add(new_num)
                    heapq.heappush(heap, new_num)
                    
        return val 
                    
