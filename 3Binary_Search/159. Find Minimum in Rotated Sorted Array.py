class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums)-1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[-1]:
                start = mid
            elif nums[mid] < nums[-1]:
                end = mid 
            else:
                end = mid 
                
        return min(nums[start], nums[end])
   

                
