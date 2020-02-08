class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code
        left, right = 0, len(s) - 1 
        while left < right:
            if s[left] == s[right]:
                left += 1 
                right -= 1
            else:
                return self.is_palindrome(s, left + 1 , right) or self.is_palindrome(s, left, right - 1)
        return True
        
    
    def is_palindrome(self, s, start, end):
        left, right = start, end 
        while left < right:
            if s[left] == s[right]:
                left += 1 
                right -= 1 
            else:
                return False 
        return True 
