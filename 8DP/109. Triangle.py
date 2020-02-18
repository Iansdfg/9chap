class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        dp = triangle
        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                left = triangle[row][col] + triangle[row + 1][col]
                right = triangle[row][col] + triangle[row + 1][col + 1]
                dp[row][col] = min(left, right)
        return dp[0][0]
