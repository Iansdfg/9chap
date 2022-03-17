class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        combinations = []
        self.dfs(n, k, 0, [], combinations)
        return combinations
        

    def dfs(self, n, k, index, combination, combinations):
        if len(combination) > k:
            return

        if len(combination) == k:
                combinations.append(combination[:])
                return

        for i in range(index, n):
            combination.append(i + 1)
            self.dfs(n, k, i + 1, combination, combinations)
            combination.pop()
