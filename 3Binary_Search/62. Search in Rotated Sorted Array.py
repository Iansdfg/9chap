class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, a, target):
        # write your code here
        if not a:
            return -1 
        
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2 
            if a[mid] <= a[end] :
                if a[mid] < target <= a[end]:
                    start = mid
                else:
                    end = mid
            else:
                if a[start] < target <= a[mid] :
                    end = mid
                else:
                    start = mid
        if a[start] == target:
            return start
        if a[end] == target:
            return end
        return -1

    
    from typing import (
    List,
)
    
#############################10/17/2022#############################

class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, a: List[int], target: int) -> int:
        # write your code here
        if not a:
            return -1
        min_pos = self.find_min(a)
        if a[min_pos] <= target <= a[-1]:
            return self.binary_search(a, min_pos, len(a)-1, target)
        else:
            return self.binary_search(a, 0, min_pos - 1, target)

    def binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

    def find_min(self, nums: List[int]) -> int:
        # write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end: 
            #Compare with end b/c its consistent
            #if array is not rotated. 
            mid = (start + end) // 2
            if nums[mid] < nums[-1]:
                end = mid 
            elif nums[mid] > nums[-1]:
                start = mid 

        if nums[start] < nums[end]:
            return start 
        else:
            return end
