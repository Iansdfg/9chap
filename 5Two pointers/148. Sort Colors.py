from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        start, mid, end = 0, 0, len(nums) - 1 

        while mid <= end:
            if nums[mid] == 0:
                nums[mid], nums[start] =  nums[start], nums[mid]
                start += 1
                mid += 1 
            elif nums[mid] == 1:
                mid += 1 
            elif nums[mid] == 2:
                nums[mid], nums[end] =  nums[end], nums[mid]
                end -= 1 

        
