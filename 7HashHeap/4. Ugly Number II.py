import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nth_ugly_number(self, n):
        # write your code here
        heap = []
        heapq.heappush(heap, 1)

        visited = set()
        visited.add(1)

        factors = [2, 3, 5]

        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for factor in factors:
                next_ugly = curr_ugly * factor 
                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(heap, next_ugly)
        return curr_ugly

