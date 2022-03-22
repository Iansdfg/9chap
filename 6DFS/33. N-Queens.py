
class Solution:
    """
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solve_n_queens(self, n):
        # write your code here
        visited = [0 for i in range(n)]
        premutations = []
        self.dfs(n, visited, [], premutations)
        premutations.sort()
        return premutations

    def dfs(self, n, visited, premutation, premutations):
        if len(premutation) == n:
            print(premutation)
            premutations.append(self.draw(premutation))
            return

        for i in range(n):
            if visited[i] == 1:
                continue
            if not self.is_valid(premutation, i):
                continue
            visited[i] = 1
            premutation.append(i)
            self.dfs(n, visited, premutation, premutations)
            premutation.pop()
            visited[i] = 0

    def is_valid(self, premutation, i):
        # (len(premutation), i) is current coordinate
        # Our goal is to check if next coordinate is valid
        # if valid, the next (row, col) and (len(premutation), i) 
        # will not bein diagonal line. 
        row, col = len(premutation), i
        for next_row, next_col in enumerate(premutation):
            if abs(row - next_row) == abs(col - next_col):
                return False
        return True 

    def draw(self, premutation):
        board = []
        for num in premutation:
            row = ['Q' if i == num else '.' for i in range(len(premutation))]
            board.append(''.join(row))
        return board


