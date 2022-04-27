class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def min_path_sum(self, grid):
        # write your code here
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue

                if col == 0:
                    dp[row][col] = dp[row - 1][col] + grid[row][col]
                    continue

                if row == 0:
                    dp[row][col] = dp[row][col - 1] + grid[row][col]
                    continue

                dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + grid[row][col]

        return dp[-1][-1]


