class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    num_to_letter = {
        '2':['a', 'b', 'c'],
        '3':['d', 'e', 'f'],
        '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'],
        '6':['m', 'n', 'o'],
        '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z']
    }
    def letter_combinations(self, digits):
        # write your code here
        if digits == '':
            return []
        combinations = []
        self.dfs(digits, 0, 0, [], combinations)
        return combinations


    def dfs(self, digits, index, level, combination, combinations):
        if len(combination) == len(digits):
            res = ''.join(combination)
            combinations.append(res)
            return
        
        num = digits[level]
        letters = self.num_to_letter[num]
        print(letters)
        for i in range(len(letters)):
            combination.append(letters[i])
            level += 1
            self.dfs(digits, i + 1, level, combination, combinations)
            level -= 1
            combination.pop()
