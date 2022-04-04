class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle):
        # write your code here
        return self.dfs(triangle, 0, 0, {})

    def dfs(self, triangle, x, y, memo):
        #return minimum path sum to bottom
        if x == len(triangle)-1:
            return triangle[x][y]
        
        if (x,y) in memo:
            return memo[(x,y)]
            
        left = self.dfs(triangle, x + 1, y, memo)
        right = self.dfs(triangle, x + 1, y + 1, memo)

        mini = min(left, right) + triangle[x][y]
        memo[(x, y)] = mini
        return mini


