class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        result = []
        self.dfs(nums, 0, [], result)
        return result
        
        
        
    def dfs(self, nums, level, path, result):
        result.append(path[:])
        
        for i in range(level, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, result)
            path.pop()
            
