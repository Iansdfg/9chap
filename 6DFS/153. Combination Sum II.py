class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
             we will sort your return value in output
    """
    def combination_sum2(self, num, target):
        # write your code here
        num.sort()
        combinations = []
        self.dfs(num, target, 0, [], combinations)
        return combinations


    def dfs(self, num, target, index, combination, combinations):
        if sum(combination) > target:
            return

        if sum(combination) == target:
            combinations.append(combination[:])
            return

        for i in range(index, len(num)):
            if i > index and num[i-1] == num[i]:
                continue
            combination.append(num[i])
            self.dfs(num, target, i + 1, combination, combinations)
            combination.pop()
