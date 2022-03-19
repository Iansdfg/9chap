class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
    """
    def k_sum_i_i(self, a, k, target):
        # write your code here
        a.sort()
        combinations = []
        self.dfs(a, k, target, 0, [], combinations)
        return combinations


    def dfs(self, a, k, target, index, combination, combinations):
        if len(combination) > k or sum(combination) > target:
            return

        if len(combination) == k and sum(combination) == target:
            combinations.append(combination[:])

        for i in range(index, len(a)):
            if i > 0 and a[i] == a[i-1]:
                continue
            combination.append(a[i])
            self.dfs(a, k, target, i + 1, combination, combinations)
            combination.pop()

