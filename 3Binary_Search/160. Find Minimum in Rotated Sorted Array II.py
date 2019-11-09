class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        while len(nums)>1 and nums[-1] == nums[0]:
            nums.pop()
            
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[-1]:
                start = mid
            elif nums[mid] < nums[-1]:
                end = mid
            else:
                end -= 1
        return min(nums[start], nums[end])
