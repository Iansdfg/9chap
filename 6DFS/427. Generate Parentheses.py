class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        string = '('*n+')'*n
        visited = [0]*n*2
        results = []
        self.dfs(string, visited, [], results)
        return results
        
    def dfs(self, string, visited, path, results):
        if len(path) == len(string) and self.is_valid(path):
            # print(path)
            results.append(''.join(path[:]))

    
        for i in range(len(string)):
            if visited[i]:
                continue 
            if i > 0 and string[i] == string[i-1] and not visited[i-1]:
                continue
            visited[i] = 1
            path.append(string[i])
            self.dfs(string, visited, path, results)
            path.pop()
            visited[i] = 0
            
    def is_valid(self, path):
        stack = []
        for char in path:
            if char == '(':
                stack.append('(')
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0 
            
        

