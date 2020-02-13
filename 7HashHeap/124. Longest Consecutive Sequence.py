class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        num_set = set(num)
        longest = 0
        for number in num:
            up = number + 1 
            while up in num_set:
                num_set.discard(up)
                up += 1
                
            low = number - 1 
            while low in num_set:
                num_set.discard(low)
                low -= 1
                
            longest = max(longest, up - low - 1)
            
        return longest
                
