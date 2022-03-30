import heapq
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kth_smallest(self, matrix, k):
        # write your code here
        heap = []
        res = None
        for row in matrix:
            if not row:
                continue
            heapq.heappush(heap, (row[0], row))

        for _ in range(k):
            curr_val, curr_row = heapq.heappop(heap)
            res = curr_val
            curr_row.pop(0)
            if not curr_row:
                continue
            heapq.heappush(heap, (curr_row[0], curr_row))

        return res



