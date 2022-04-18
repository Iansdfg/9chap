class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1 
        res = 0

        while left < right:
            twoSum = nums[left] + nums[right]
            if twoSum < target:
                left += 1 
            elif twoSum > target:
                right -= 1 
            else:
                print(left, right)
                res += 1 
                left += 1 
                right -= 1 


            #最后去重， 否则会多算 eg# ‘2,2,2,2,2’ 中间的2会多算一次
            while left < right and left > 0 and nums[left] == nums[left - 1]:
                left += 1 
            while left < right and right < len(nums) - 1 and nums[right] == nums[right + 1]:
                right -= 1

        return res 



    class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        start, end = 0, len(nums) - 1 
        cnt = 0
        last_part = (-1, -1)
        while start < end:
            value = nums[start] + nums[end] 
            if target > value:
                start += 1 
            elif target < value:
                end -= 1 
            else:
                if last_part != (nums[start] , nums[end]):
                    cnt += 1 
                    last_part = (nums[start] , nums[end])
                start += 1 
                end -= 1 
        return cnt


