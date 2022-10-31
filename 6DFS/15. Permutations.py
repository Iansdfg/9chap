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

            
            
###################################################10/30/2022##############################################
from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        permutations = []
        visited = set()
        self.dfs(nums, visited, [], permutations)
        return permutations


    def dfs(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            print(permutation)
            permutations.append(permutation[:])
            return

        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            permutation.append(nums[i])
            visited.add(nums[i])
            self.dfs(nums, visited, permutation, permutations)
            visited.remove(nums[i])
            permutation.pop()
            

