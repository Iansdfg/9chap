class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        results = []
        visited = [0]*n
        self.dfs(n, visited, [], results)
        return results
        
    def dfs(self, n, visited, path, results):
        if len(path) == n:
            board = self.makeboard(path[:])
            results.append(board)
            return
        
        for i in range(n):
            if visited[i]:
                continue
            if not self.is_valid(path, i):
                continue
            visited[i] = 1
            path.append(i)
            self. dfs(n, visited, path, results)
            path.pop()
            visited[i] = 0
            
    def is_valid(self, cols, target_col):
        target_row = len(cols)
        for curr_r, curr_c in enumerate(cols):
            if curr_c == target_col:
                return False
            if curr_r - curr_c == target_row - target_col or curr_r + curr_c == target_row + target_col:
                return False
        return True
        
    def makeboard(self, path):
        n = len(path)
        board = []
        for num in path:
            row = []
            for i in range(n):
                if i == num:
                    row.append('Q')
                else:
                    row.append('.')
            board.append(''.join(row))
        return board
