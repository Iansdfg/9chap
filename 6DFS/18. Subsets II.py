class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
             we will sort your return value in output
    """
    def subsets_with_dup(self, nums):
        # write your code here
        nums.sort()
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets


    def dfs(self, nums, index, path, subsets):
        subsets.append(path[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path, subsets)
            path.pop()
