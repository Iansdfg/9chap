class Solution:
    """
    @param n: An integer
    @return: a list of combination
             we will sort your return value in output
    """
    def get_factors(self, n):
        # write your code here
        factors = []
        self.dfs(2, n, [], factors)
        return factors

    import math
    def dfs(self, start, n, factor, factors):
        if n <=1:
            if len(factor) > 1:
                print(factor)
                factors.append(sorted(factor[:]))
            return 

        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i != 0:
                continue
            factor.append(i)
            self.dfs(i, n/i, factor, factors)
            factor.pop()

        if n >= start:
            factor.append(n)
            self.dfs(n, 1, factor, factors)
            factor.pop()
