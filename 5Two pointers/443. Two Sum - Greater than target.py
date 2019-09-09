class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        ans = 0
        left, right = 0, len(nums)-1
        while left<right:
            two_sum = nums[left]+nums[right]
            if two_sum>target:
                ans += right-left
                right-=1
            else:
                left+=1
        return ans
            
