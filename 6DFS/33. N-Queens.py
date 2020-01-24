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
            chessboard = self.draw_chessboard(path)
            results.append(chessboard)
            
            return
        
        for i in range(n):
            if visited[i]:
                continue
            
            if not self.is_valid(path, len(path), i):
                continue
            
            visited[i] = 1
            path.append(i)
            self.dfs(n, visited, path, results)
            path.pop()
            visited[i] = 0
            
    def is_valid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
        return True
        
    def draw_chessboard(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
            
    
