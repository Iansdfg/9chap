class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def two_sum(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            twoSum = nums[left] + nums[right]
            if twoSum > target:
                right -= 1 
            elif twoSum < target:
                left += 1 
            else:
                return [left + 1, right + 1]
            

