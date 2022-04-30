class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """

    def max_submatrix(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        prefix_sum = self.get_prefix_sum(matrix)
        max_sum = float('-inf')

        for up in range(self.rows):
            for down in range(up, self.rows):
                arr = self.compression(matrix, up, down, prefix_sum)
                max_sum = max(max_sum, self.max_sub_array(arr))
        return max_sum

    
    def get_prefix_sum(self, matrix):
        prefix_sum = [[0 for _ in range(self.cols)] for _ in range(self.rows + 1)]

        for row in range(self.rows):
            for col in range(self.cols):
                prefix_sum[row + 1][col] = prefix_sum[row][col] + matrix[row][col]
        return prefix_sum

    def compression(self, matrix, up, down, prefix_sum):
        arr = [0 for _ in range(self.cols)]
        for i in range(self.cols):
            arr[i] = prefix_sum[down + 1][i] - prefix_sum[up][i]
        return arr

    def max_sub_array(self, nums):
        # write your code here
        #dp[i] = max(nums[:i])
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)
