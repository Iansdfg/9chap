class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    KEYBOARD = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
    def letterCombinations(self, digits):
        # write your code here
        if digits == '':
            return []
        results = []
        self.dfs(digits, 0, [], results)
        return results
        
    def dfs(self, digits, index, path, results):
        if len(path) == len(digits):
            results.append(''.join(path[:]))
            return
        
        for letter in self.KEYBOARD[digits[index]]:
            path.append(letter)
            self.dfs(digits, index+1, path, results)
            path.pop()
