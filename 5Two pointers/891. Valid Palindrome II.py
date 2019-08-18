class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        l, r = 0, len(s)-1
        
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                break
        
        delet_l = s[:l]+s[l+1:]
        delet_r = s[:r]+s[r+1:]
        
        return delet_l==delet_l[::-1] or delet_r==delet_r[::-1]
