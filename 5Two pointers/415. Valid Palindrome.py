class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s):
        # write your code here
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1 
            while start < end and not s[end].isalnum():
                end -= 1 
            print(s[start], s[end])
            if start < end and s[start].lower() !=  s[end].lower():
                return False 
            start += 1 
            end -= 1 
        return True 


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while start < end:
            
            while not s[start].isalnum() and start < len(s)-1 and start < end:
                start += 1 
            while not s[end].isalnum() and end > 0 and start < end:
                end -= 1 
            
            if s[start].lower() == s[end].lower():
                start += 1 
                end -= 1 
            else:
                return False
        return True 


        
