class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        results = []
        visited = [0] * len(nums)
        self.dfs(nums, [], results, visited)
        return results
        
        
    def dfs(self, nums, path, results, visited):
        if len(path) == len(nums):
            results.append(path[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            path.append(nums[i])
            visited[i] = 1 
            self.dfs(nums, path, results, visited)
            visited[i] = 0
            path.pop()
