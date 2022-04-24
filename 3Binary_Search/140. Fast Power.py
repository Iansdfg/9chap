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
