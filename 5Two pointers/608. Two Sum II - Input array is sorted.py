class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def two_sum(self, nums, target):
        # write your code here
        start, end = 0, len(nums) - 1
        while start < end:
            value = nums[start] + nums[end]
            if value > target:
                end -= 1 
            elif value < target:
                start += 1 
            else:
                return [start + 1, end + 1]
        return []
