class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        rows, cols = len(grid), len(grid[0])
        if rows == 0 or cols == 0:
            return 0
    
        dp = grid
        
        for row in range(rows):
            for col in range(cols):
                if col == row == 0:
                    dp[row][col] = grid[row][col]
                elif row == 0:
                    dp[row][col] = dp[row][col - 1] + grid[row][col]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col] + grid[row][col]
                else:
                    up = dp[row - 1][col] + grid[row][col]
                    left = dp[row][col - 1] + grid[row][col]
                    dp[row][col] = min(up, left)
                    
        return dp[-1][-1]
