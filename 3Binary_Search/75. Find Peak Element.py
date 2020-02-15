class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left, right = 0, len(A) - 1 
        while left + 1 < right:
            mid = (left + right) // 2 
            if mid == 0 or mid == len(A) - 1:
                return mid
            if A[mid-1] < A[mid] < A[mid+1]:
                left = mid 
            elif A[mid-1] > A[mid] > A[mid+1]:
                right = mid 
            elif A[mid-1] > A[mid] and A[mid] < A[mid+1]:
                right = mid
            else:
                return mid 
