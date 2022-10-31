from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        nums.sort()
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, index, subset, subsets):
        print(subset)
        subsets.append(subset[:])

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()
