class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        string  = ''
        
        for char in s:
            if char.isalnum():
                
                if char.isdigit():
                    string += char
                else:
                    string += char.lower()
                    
        return string[:] == string[::-1]
