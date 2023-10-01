import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if not piles:return 0
        start, end = 1, max(piles)
        while start + 1 < end:
            mid = (start + end) // 2
            print("mid ", mid, self.check(mid, piles))
            if self.check(mid, piles) > h:
                start = mid
            elif self.check(mid, piles) <= h:
                end = mid 
        if self.check(start, piles) <= h:
            return start
        elif self.check(end, piles) <= h:
            print('end', self.check(end, piles) <= h)
            return end
        return -1

    def check(self, k, piles):
        h = 0
        for pile in piles:
            h += math.ceil(float(pile)/k)
        return h
