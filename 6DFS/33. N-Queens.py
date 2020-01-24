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
            # results.append(path[:])
            return
        
        for i in range(n):
            if visited[i]:
                continue
            
            if not self.is_valid(path, i):
                continue
            
            visited[i] = 1
            path.append(i)
            self.dfs(n, visited, path, results)
            path.pop()
            visited[i] = 0
            
    def is_valid(self, path, i):
        len_path = len(path)
        for pos, val in enumerate(path):
            # 两个点在斜线上的判断方式用一个等式
            # Math.abs(x1 - x2) == Math.abs(y1 - y2) 即可。
            # 根据x1 + y1 == x2 + y2 和 x1 - y1 == x2 - y2
            if pos - val == len_path - i or pos + val == len_path + i:
                return False
        return True
        
    def draw_chessboard(self, path):
        n = len(path)
        board = []
        for i in range(n):
            row = ['Q' if j == path[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
            
    
