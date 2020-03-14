class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        start, end = 0, len(A) - 1 
        self.helper(A, start, end)
        
    def helper(self, A, start, end):
        print(start, end)
        if start >= end:
            return 
        
        left, right = start, end
        pivit = A[(left + right)//2]
        
        while left <= right:
            while left <= right and A[left] < pivit:
                left += 1 
            while left <= right and A[right] > pivit:
                right -= 1 
                
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1 
                right -= 1 
                
        self.helper(A, start, right)
        self.helper(A, left, end)
