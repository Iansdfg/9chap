from typing import (
    List,
)

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        # write your code here
        start, end = 0, len(nums) - 1

        while start + 1 < end: 
            mid = (start + end) // 2 
            if nums[mid-1] < nums[mid]:
                start = mid 
            elif nums[mid-1] > nums[mid]:
                end = mid 
            
        if nums[end] > nums[start]:
            return nums[end]
        else:
            return  nums[start]
            
