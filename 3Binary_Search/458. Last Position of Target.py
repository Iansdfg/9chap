class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if len(nums)==0:
            return -1
        left, right = 0, len(nums)-1
        while left+1<right:
            mid = (left+right)//2
            if nums[mid]>target:
                right = mid
            elif nums[mid]<target:
                left = mid
            else:
                left = mid
                
        if nums[right]==target:
            return right
        elif nums[left]==target:
            return left
        else:
            return -1
