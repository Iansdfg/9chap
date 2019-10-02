class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        left, right = 0, len(A)-1
        last = 0
        while left+1<right:
            mid = (left+right) // 2
            if A[mid]==target:
                return mid
            elif A[mid]>target:
                right = mid
            elif A[mid]<target:
                left = mid
        return left if abs(A[left]-target)<abs(A[right]-target) else right
