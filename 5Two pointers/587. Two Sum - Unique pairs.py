class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums)-1
        res = 0
        while left<right:
            two_sum = nums[left]+nums[right]
            if two_sum == target:
                res += 1
                left,right = left+1,right-1
                while left<right and nums[left] == nums[left-1]:
                    left+=1
                while left<right and nums[right] == nums[right+1]:
                    right-=1
            elif two_sum<target:
                left+=1
            elif two_sum>target:
                right-=1
        return res
