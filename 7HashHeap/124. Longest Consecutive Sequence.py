class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        if len(num) <= 1:
            return len(num)
        nums_set = set(num)
        res = float('-inf')
         
        for number in num:
            count = 1
            
            up = number+1
            while up in nums_set:
                nums_set.discard(up)
                up += 1
                count += 1 
                
            low = number-1
            while low in nums_set:
                nums_set.discard(low)
                low -= 1
                count += 1
                
            res = max(res, count)
        return res  
                
                
                
