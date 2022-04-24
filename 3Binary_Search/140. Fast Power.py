class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a, b, n):
        # write your code here
        base = a
        ans = 1
        while n:
            if n % 2:
                ans = (base * ans)%b

            n = n // 2
            base  = (base ** 2)%b

        return ans % b

    
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a, b, n):
        # write your code here
        if n == 0:
            return 1%b
        if n == 1:
            return a%b 

        power = self.fast_power(a, b, n//2)
        power = (power * power) % b 
        
        if n % 2: 
            power = (power * a) % b
        
        return power
