class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num.sort()
        results = []
        self.dfs(num, target, 0, [], results)
        return results
        
    def dfs(self, num, target, index, path, results):
        if sum(path) > target:
            return
        
        if sum(path) == target:
            results.append(path[:])
            
        for i in range(index, len(num)):
            if i > index and num[i] == num[i - 1]:
                continue
            
            path.append(num[i])
            self.dfs(num, target, i + 1, path, results)
            path.pop()
