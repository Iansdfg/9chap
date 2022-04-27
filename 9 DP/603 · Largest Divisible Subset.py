####### O(n^2) #######
from typing import (
    List,
)

class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    
    
    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        # write your code here
        nums.sort()
        #dp: max # of elements of factors 
        dp = [1 for i in range(len(nums))]
        #prev: dp[prev[i]] + 1 = dp[i]
        prev = [-1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                     dp[i] = dp[j] + 1 
                     prev[i] = j

        last = 0 #last index of LIS
        max_val = float('-inf')
        for i in range(len(dp)): 
            if dp[i] > max_val:
                max_val = dp[i]
                last = i

        return self.get_order(nums, prev, last)

    def get_order(self, nums, prev, last_index):
        order = []
        while last_index != -1:
            order.append(nums[last_index])
            last_index = prev[last_index]
        return order[::-1]
        


        

