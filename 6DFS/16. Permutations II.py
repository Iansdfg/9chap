class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        results = []
        visited = [0]*len(nums)
        self.dfs(nums, [], results, visited)
        return results
        
    def dfs(self, nums, path, results, visited):
        if len(nums) == len(path):
            results.append(path[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            
            path.append(nums[i])
            visited[i] = 1
            self.dfs(nums, path, results, visited)
            visited[i] = 0
            path.pop()
            
