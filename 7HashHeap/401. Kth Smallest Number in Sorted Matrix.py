from heapq import heappop, heappush
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here

        heap = []
        for row_num, row in enumerate(matrix):
            if row == []:
                continue
            heappush(heap, (matrix[row_num][0], row_num, 0))
        
        ans = matrix[0][0]
        for _ in range(k):
            curr_val, curr_row, curr_col = heappop(heap)
            ans = curr_val
    
            next_col = curr_col + 1 
            if next_col >= len(matrix[curr_row]):
                continue
            heappush(heap, (matrix[curr_row][next_col], curr_row, next_col))
        return ans 
