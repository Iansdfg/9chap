class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
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
            
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            
            visited[i] = 1 
            path.append(nums[i])
            self.dfs(nums, visited, path, results)
            path.pop()
            visited[i] = 0
        
