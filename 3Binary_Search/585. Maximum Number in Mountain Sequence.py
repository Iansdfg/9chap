class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums):
        # write your code here
        if not nums:
            return -1

        start, end = 0, len(nums) - 1 

        while start + 1 < end:
            mid = (start + end) // 2 

            if nums[mid] >= nums[mid + 1]:
                end = mid
            elif nums[mid] <= nums[mid + 1]:
                start = mid
        
        return max(nums[start], nums[end])
