class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
            
        if n == 0:
            return 1%b
        
        if n%2:
            ans = self.fastPower(a, b, n//2)
            return (a*(ans*ans))%b
        else:
            ans = self.fastPower(a, b, n//2)
            return (ans*ans)%b
