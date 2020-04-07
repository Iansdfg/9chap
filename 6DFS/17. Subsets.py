class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        results = []
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, index, path, results):
        results.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, results)
            path.pop()
            
