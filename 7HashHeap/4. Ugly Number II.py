from heapq import heapify, heappop, heappush

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        
        heap = [1]
        heapify(heap)
        visited = set([])
        
        for i in range(n):
            
            val = heappop(heap)
            for factor in [2, 3, 5]:
                new_val = factor * val
                
                if new_val not in visited:
                    visited.add(new_val)
                    heappush(heap, new_val)
                    
        return val
