from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums: return -1
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end)//2

            if target > nums[mid]:
                start = mid 
            if target <= nums[mid]:
                end = mid 

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end 
        return -1
            
            



