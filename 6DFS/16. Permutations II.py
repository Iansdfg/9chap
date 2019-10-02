class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
        nums.sort()
        visited = [0]*len(nums)
        ans = []
        self.dfs( nums, visited, [], ans)
        return ans
        
    def dfs(self, nums, visited, path, ans):
        if len(path) == len(nums):
            ans.append(path[:])
            return 
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            path.append(nums[i])
            visited[i]=1
            self.dfs(nums, visited, path, ans)
            visited[i]=0
            path.pop()
       
