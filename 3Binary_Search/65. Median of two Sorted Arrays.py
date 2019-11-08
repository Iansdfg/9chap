class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        length = len(A) + len(B)
        if length % 2 == 0:
            return (self.find_kth(A, B, length // 2) + self.find_kth(A, B, length // 2 + 1)) / 2
        return self.find_kth(A, B, length//2 + 1)
        
    def find_kth(self, A, B, k):     
        if len(A) == 0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]
        start, end = min(A[0], B[0]), max(A[-1], B[-1])
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.count_small_or_equal(A, mid) + self.count_small_or_equal(B, mid) < k:
                start = mid 
            elif self.count_small_or_equal(A, mid) + self.count_small_or_equal(B, mid) > k:
                end = mid
            else:
                end = mid

        if self.count_small_or_equal(A, start) + self.count_small_or_equal(B, start) == k:
                return start
        return end
        
    # find first index that arr[index] > target
    def count_small_or_equal(self, arr, target):
        
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] < target: 
                start = mid 
            elif arr[mid] == target:
                start = mid 
            else:
                end = mid 
            
        if arr[start] > target:
            return start
        if arr[end] > target:
            return end
        return len(arr)
    

            
