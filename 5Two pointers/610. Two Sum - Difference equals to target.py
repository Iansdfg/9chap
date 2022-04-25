class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums, target):
        # write your code here
        nums.sort()
        if len(nums) <= 1:
            return [-1, -1]

        left, right = 0, 1
        while right < len(nums):
            if nums[right] - nums[left] < target:
                right += 1 
            elif nums[right] - nums[left] > target:
                left += 1 
            else:
                return [min(nums[left], nums[right]), max(nums[left], nums[right])]
            if left == right:
                left += 1 
        return [-1, -1]
