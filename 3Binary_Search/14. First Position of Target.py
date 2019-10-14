class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid]<target:
                left = mid
            elif nums[mid]>target:
                right = mid
            else:
                right = mid
                
        if nums[left] == target:
            return left 
        elif nums[right] == target:
            return right
        else:
            return -1
                
            
