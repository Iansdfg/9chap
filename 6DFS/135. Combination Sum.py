class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return[[]]
        candidates.sort()
        results = []
        self.dfs(candidates, target, [], results)
        return results
        
    def dfs(self, candidates, target, path, results):
        if sum(path) > target:
            return
        if sum(path) == target:
            results.append(path[:])
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            self.dfs(candidates[i:], target, path, results)
            path.pop()
        
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return[[]]
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results
        
    def dfs(self, candidates, target, index, path, results):
        if target < 0:
            return
        if  target == 0:
            results.append(path[:])
            return
        for i in range(index, len(candidates)):

            path.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, path, results)
            path.pop()
        
