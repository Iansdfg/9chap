class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def splitArray(self, nums, m):
        # write your code here
        left, right = max(nums), sum(nums)
        
        while left + 1 < right:
            mid = (left + right)//2
            # num of m when mid is largest sum
            if self.num_of_array(nums, mid) <= m:
                right = mid
            elif self.num_of_array(nums, mid) > m:
                left = mid
                
        if self.num_of_array(nums, left) <= m:
            return left
        else:
            return right
            
    def num_of_array(self, nums, target):
        # return max sub array number when sum of one arrary is less than target
        curr_sum = 0
        num_of_array = 0
        
        for num in nums:
            if curr_sum + num <= target:
                curr_sum += num
            else:
                num_of_array += 1
                curr_sum = num
        num_of_array += 1
        return num_of_array
