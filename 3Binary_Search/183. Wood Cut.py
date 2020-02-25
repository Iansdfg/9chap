class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
            
        left, right = 1, max(L)
        
        while left + 1 < right:
            mid = (left + right) // 2
            if self.get_piece(mid, L) >= k:
                left = mid
            else:
                right = mid
        
        if self.get_piece(left, L) >= k:
            return left
        elif self.get_piece(right, L) >= k:
            return right
        return 0
            
    def get_piece(self, length, L):
        return sum([piece//length for piece in L])
        

            
