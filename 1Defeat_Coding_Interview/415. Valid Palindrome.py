class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        left, right = 0, len(s) - 1 
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1 
            while left < right and not s[right].isalnum():
                right -= 1 
            if left < right and s[right].lower() != s[left].lower():
                return False 
            left += 1 
            right -= 1 
        return True 
            
