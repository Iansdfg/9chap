class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        str = sorted(str)
        results = []
        visited = [0] * len(str)
        self.dfs(str, visited, [], results)
        return results
        
    def dfs(self, str, visited, path, results):
        
        if len(path) == len(str):
            # print(path)
            results.append(''.join(path[:]))
            return
        
        for i in range(len(str)):
            
            if visited[i]:
                continue
            
            if i>0 and str[i] == str[i - 1] and not visited[i - 1]:
                continue
            
            visited[i] = 1 
            path.append(str[i])
            self.dfs(str, visited, path, results)
            path.pop()
            visited[i] = 0
            
