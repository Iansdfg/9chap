class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        results = []
        self.dfs(n, k, 0, [], results)
        return results
        
    def dfs(self, n, k, index, path, results):
        if len(path) == k:
            results.append(path[:])
            return
        
        for i in range(index+1, n+1):
            path.append(i)
            self.dfs(n, k, i, path, results)
            path.pop()
