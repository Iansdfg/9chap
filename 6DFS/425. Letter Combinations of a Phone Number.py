num_to_alpa = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxzy'
        }
        
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if digits == '':
            return []
            
        results = []
        self.dfs(digits, [], results)
        return results
        
    def dfs(self, digits, path, results):
        if digits == '':
            results. append(''.join(path))
            return
            
        chars = num_to_alpa[digits[0]]
        for i in range(len(chars)):
            path.append(chars[i])
            self.dfs(digits[1:], path, results)
            path.pop()
