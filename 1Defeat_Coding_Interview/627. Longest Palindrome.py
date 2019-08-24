class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        chars = []
        res = 0
        for char in s:
            if char in chars:
                chars.remove(char)
                res+=1
     
            else:
                chars.append(char)
                
        return min(res*2+1, len(s))
            
