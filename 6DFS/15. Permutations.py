class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums):
        # write your code here

        permutions = []
        visited = set()
        self.dfs(nums, visited, [], permutions)
        return permutions
    
    def dfs(self, nums, visited, permution, permutions):
        if len(permution) == len(nums):
            permutions.append(permution[:])
            return

        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            permution.append(nums[i])
            visited.add(nums[i])
            self.dfs(nums, visited, permution, permutions)
            visited.remove(nums[i])
            permution.pop()

            
            
