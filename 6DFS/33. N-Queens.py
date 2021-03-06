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
        # len_path is x, i is y 
        # pos of path is row, val of path is col
        # determian if abs(x - row) == abs(y - col)
        for row, col in enumerate(path):
            # 两个点在斜线上的判断方式用一个等式
            # Math.abs(x - row) == Math.abs(y - col) 即可。
            # 根据x + row == y + col 和 x - row == y - col
            if row - col == len_path - i or row + col == len_path + i:
                return False
        return True
        
    def draw_chessboard(self, path):
        board = []
        for ele in path:
            row = ['Q' if i == ele else '.' for i in range(len(path))]
            # row = []
            # for i in range(len(path)):
            #     if i == ele:
            #         row.append('Q') 
            #     else: 
            #         row.append('.') 
            board.append(''.join(row))
        return board
            
