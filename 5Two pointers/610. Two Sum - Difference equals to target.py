class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums, target):
        # write your code here
        target = abs(target)
        start, end = 0, 1
        while end < len(nums):
            if nums[end] - nums[start] == target:
                return [nums[start], nums[end]]
            elif nums[end] - nums[start] < target:
                end += 1 
            elif nums[end] - nums[start] > target:
                start += 1 
                end = max(start + 1, end)
        return [-1, -1]
