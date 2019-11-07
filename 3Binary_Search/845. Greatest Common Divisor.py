class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        big, small = max(a, b), min(a, b)
        
        # if small == 0:
        #     return big
        # return self.gcd(big % small, small) 
        
        while small:
            small, big = big % small, small
        return big
