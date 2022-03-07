class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums):
        # write your code here
        if not nums:
            return -1
        start, end  = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2 
            #Compare with end b/c its consistent
            #if array is not rotated. 
            #If compare with start, the answer is 
            #wrong if not rotated.
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid

        return min(nums[start], nums[end])
