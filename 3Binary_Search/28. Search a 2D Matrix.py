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

from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        # write your code here
        start, end = 0, len(matrix)-1

        target_role_id = -1
        while start + 1 < end:
            mid = (start + end) // 2 
            if target > matrix[mid][-1]:
                start = mid 
            elif target < matrix[mid][0]:
                end = mid 
            else:
                target_role_id = mid
                break
        
        if matrix[start][0] <= target <= matrix[start][-1]:
            target_role_id = start
        elif matrix[end][0] <= target <= matrix[end][-1]:
            target_role_id = end
        elif target < matrix[start][0] and target > matrix[end][-1]:
            return False 
        
        target_role =  matrix[target_role_id]

        start, end = 0, len(target_role)-1
        while start + 1 < end:
            mid = (start + end) // 2 
            if target > target_role[mid]:
                start = mid 
            elif target < target_role[mid]:
                end = mid 
            else:
                return True 
        
        if target_role[start] == target or target_role[end] == target:
            return True 
        return False 

        

