class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0:
            return [-1, -1]
        fist = self.find_first( A, target)
        last = self.find_last( A, target)
        return [fist, last]
        
        
        
    def find_first(self, A, target):
        start, end = 0, len(A)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
            elif A[mid] == target:
                end = mid
            
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1
            
    
    def find_last(self, A, target):
        start, end = 0, len(A)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
            elif A[mid] == target:
                start = mid
            
        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        else:
            return -1
