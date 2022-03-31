class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle):
        # write your code here
        memo = dict()
        return self.divide_conqure(triangle , 0, 0, memo)

    def divide_conqure(self, triangle , x, y, memo):
        if x == len(triangle):
            return 0

        if (x, y) in memo:
            return memo[(x, y)]
        left = self.divide_conqure(triangle , x + 1, y, memo)
        right = self.divide_conqure(triangle , x + 1, y + 1, memo)

        memo[(x, y)] = min(left, right) + triangle[x][y]

        return memo[(x, y)]



