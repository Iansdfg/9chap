class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        return self.quick_sort(A, 0, len(A)-1)
            
    def quick_sort(self, A, start, end):
        
        if start >= end:
            return
        
        left, right = start, end
        
        pivot = A[(start+end)//2]
        
        while left<=right:
            while left<=right and pivot>A[left]:
                left+=1
            
            while left<=right and pivot<A[right]:
                right-=1
                
            if left<=right:
                A[right], A[left] = A[left],A[right]
                
                right-=1
                left+=1
        
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)
       
