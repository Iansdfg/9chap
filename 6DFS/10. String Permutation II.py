class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        s = sorted(list(str))
        results = []
        visited = [0]*len(s)
        self.dfs(s, visited, [], results)
        return results
        
    def dfs(self, s, visited, path, results):
        if len(s) == len(path):
            results.append(''.join(path))
            return
        
        for i in range(len(s)):
            if visited[i]:
                continue
            
            if i>0 and s[i]==s[i-1] and not visited[i-1]:
                continue
            
            
            path.append(s[i])
            visited[i] = 1
            
            self.dfs(s, visited, path, results)
            visited[i] = 0
            path.pop()
            
        
        
