class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        visited = [0 for i in range(len(nums))]
        permutations = []
        self.dfs(nums, visited, [], permutations)
        return permutations

    def dfs(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
           permutations.append(permutation[:])
           return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            permutation.append(nums[i])
            visited[i] = 1
            self.dfs(nums, visited, permutation, permutations)
            visited[i] = 0
            permutation.pop()

            
            
