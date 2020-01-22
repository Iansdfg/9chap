class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        nums.sort()
        results = []
        visited = [0] * len(nums)
        self.dfs(nums, visited, [], results)
        return results
        
    def dfs(self, nums, visited, path, results):
        if len(path) == len(nums):
            results.append(path[:])
            
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            visited[i] = 1 
            path.append(nums[i])
            self.dfs(nums, visited, path, results)
            path.pop()
            visited[i] = 0
            
