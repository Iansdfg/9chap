class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s):
        # write your code here
        visited = set()
        cnt = 0
        for char in s:
            if char in visited:
                visited.remove(char)
                cnt += 1 
            else:
                visited.add(char)

        length = cnt * 2 
        if visited:
            return length + 1 
        return length
            
