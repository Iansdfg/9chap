class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        base, ans = a, 1 
        while n:
            if n%2:
                ans = (base * ans) % b
            base =(base*base) % b 
            n //= 2 
        return ans % b 
