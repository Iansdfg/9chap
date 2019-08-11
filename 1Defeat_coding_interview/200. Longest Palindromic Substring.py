class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if len(s)<2: return s
        maxx = ''
        for i in range(1, len(s)):
            sub = self.findPal(i, i,s)
            if len(sub)>len(maxx):
                maxx = sub
            sub = self.findPal(i, i-1,s)
            if len(sub)>len(maxx):
                maxx = sub
        return maxx

    
    def findPal(self, l,r,s):
        while l>=0 and r<= len(s)-1 and s[l] == s[r]:
            l-=1
            r+=1
            # print(l,r)
        return s[l+1:r]
