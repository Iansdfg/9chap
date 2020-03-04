class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if len(s) < 2:
            return s 
            
        max_pal = ''
        for i in range(1, len(s)):
            pal = self.find_palindro(s, i-1, i)
            if len(pal) > len(max_pal):
                max_pal = pal
                
            pal = self.find_palindro(s, i, i)
            if len(pal) > len(max_pal):
                max_pal = pal
                
        return max_pal
                
    def find_palindro(self, s, l, r):
        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            l -= 1 
            r += 1
        # print(l,r)
        return s[l + 1: r]
