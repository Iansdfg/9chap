class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        memo = dict()
        return self.isMatch_helper(0, 0, s, p, memo)
        
    def isMatch_helper(self, i, j, source, pattern, memo):
        if (i, j) in memo:
            return memo[(i, j)]
            
        if len(source) == i:
            for index in range(j, len(pattern)):
                if pattern[index] != '*':
                    return False 
            return True 
            
        if len(pattern) == j:
            return False 
            
        if pattern[j] == '*':
            matched = self.isMatch_helper(i + 1, j, source, pattern, memo) or self.isMatch_helper(i, j + 1, source, pattern, memo)
        else:
            matched = self.isMatch_helper(i + 1, j + 1, source, pattern, memo) and self.is_char_match(source[i], pattern[j])
            
        memo[(i, j)] = matched
        return matched
        
    def is_char_match(self, s, p):
        return s == p or p == '?'
        
            
            
        
