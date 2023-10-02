from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1 

        while start + 1 < end: 
            mid = (start + end)//2 
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            # There will be no  nums[mid] = nums[end] case,
            # There will be at lease 2 num before it jump out of loop,
            # And // will only make nums[mid] = nums[start]
        return min(nums[start],nums[end])
