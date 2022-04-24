class Solution:
    """
    @param s: a string to be split
    @return: all possible split string array
    """
    def split_string(self, s):
        # write your code here
        combinations = []
        self.dfs(s, [], combinations)
        return combinations

    def dfs(self, s, combination, combinations):
        if s == '':
            combinations.append(combination[:])
            return

        for i in range(1, 3):
            if i > len(s):
                continue
            combination.append(s[:i])
            self.dfs(s[i:], combination, combinations)
            combination.pop()


