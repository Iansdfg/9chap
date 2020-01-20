class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        str = sorted(str)
        visited = [0] * len(str)
        results = []
        self.dfs(str, [], results, visited)
        return results
        
        
    def dfs(self, str, path, results, visited):
        
        if len(path) == len(str):
            results.append(''.join(path[:]))
            
        for i in range(len(str)):
            
            if visited[i]:
                continue
            
            if i > 0 and str[i] == str[i-1] and not visited[i-1]:
                continue
            
            path.append(str[i])
            visited[i] = 1
            self.dfs(str, path, results, visited)
            visited[i] = 0
            path.pop()
            
        
