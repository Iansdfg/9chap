class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsets_with_dup(self, nums):
        # write your code here
        subsets = []
        nums.sort()
        self.dfs(nums, 0, [], subsets)
        return subsets


    def dfs(self, nums, index, subset, subsets):
        subsets.append(subset[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()
