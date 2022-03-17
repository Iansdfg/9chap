class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        paths = []
        self.dfs(nums, 0, [], paths)
        return paths


    def dfs(self, nums, index, path, paths):
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, paths)
            path.pop()

