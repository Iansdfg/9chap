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
