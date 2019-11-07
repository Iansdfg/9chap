import math

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        res = []
        up = math.sqrt(num)
        
        k = 2
        while k <= up and num > 1:
            while not num % k:
                num //= k
                res.append(k)
            k += 1
            
        if num > 1:
            res.append(num)
        return res
