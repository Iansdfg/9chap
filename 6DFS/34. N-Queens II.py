class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        results =[]
        visited = [0]*n
        self.dfs(n, visited, [], results)
        return len(results)
        
    def dfs(self, n, visited, path, results):
        if len(path) == n:
            results.append(path[:])
            
        for i in range(n):
            if visited[i]:
                continue
            
            if not self.is_valid(i, path):
                continue
            
            visited[i] = 1 
            path.append(i)
            self.dfs(n, visited, path, results)
            path.pop()
            visited[i] = 0
            
    def is_valid(self, i, path):
        path_len = len(path)
        for pos, val in enumerate(path):
            if pos - val == path_len - i or pos + val == path_len + i :
                return False 
        return True 
        
        
