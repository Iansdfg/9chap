class Solution:
    """
    @param obstacle_grid: A list of lists of integers
    @return: An integer
    """
    def unique_paths_with_obstacles(self, obstacle_grid):
        # write your code here
        rows = len(obstacle_grid)
        cols = len(obstacle_grid[0])

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        if obstacle_grid[0][0] == 0:
            dp[0][0] = 1 
        for row in range(rows):
            for col in range(cols):
                if obstacle_grid[row][col]:
                    continue 

                if col == 0 and row == 0: 
                    continue 

                if col == 0:
                    dp[row][col] = dp[row - 1][col]
                    continue

                if row == 0:
                    dp[row][col] = dp[row][col - 1]
                    continue

                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]
                
