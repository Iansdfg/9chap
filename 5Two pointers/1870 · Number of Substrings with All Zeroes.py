class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def string_count(self, str):
        # Write your code here.
        slow,fast = 0, 0 
        res = 0
        while slow < len(str):
            if str[slow] == '0':
                fast = slow 
                while fast < len(str) and str[fast] == '0':
                    fast += 1 
                num_of_zero = fast - slow
                if num_of_zero:
                    res += (num_of_zero * (num_of_zero+1))//2
                slow = fast
            slow += 1
        return res 
