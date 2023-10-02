from typing import (
    List,
)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end: 
            mid = (start + end) // 2
            if nums[mid] == target:
                    return mid
            if nums[mid] > nums[end]:
                if nums[end] < target < nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[end]:
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
        
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1
    
