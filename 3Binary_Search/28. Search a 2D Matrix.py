class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if  matrix == [] or matrix == [[]]:
            return False
        start, end = 0, len(matrix)-1

        while start + 1 < end:
            mid = (start + end) // 2
            if target < matrix[mid][0]:
                end = mid
            elif target > matrix[mid][-1]:
                start = mid 
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                end = mid 
                
        if target in matrix[start] or target in matrix[end]:
            return True
        return False
