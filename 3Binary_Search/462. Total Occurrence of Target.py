class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if len(A)==0:
            return 0
        fist_pos = self.findFirst(A, target)
        Last_pos = self.findLast(A, target)
        if fist_pos is None or Last_pos is None:
            return 0
        else:
            return Last_pos-fist_pos+1
        return fist_pos
        
    def findFirst(self, A, target):
        left, right = 0, len(A)-1
        while left+1<right:
            mid = (left+right) // 2
            if A[mid] > target:
                right = mid
            elif  A[mid] < target:
                left = mid
            else:
                right = mid

        if A[left] == target:
            return left
        elif A[right] == target:
            return right
        else:
            return None
            
    def findLast(self, A, target):
        left, right = 0, len(A)-1
        while left+1<right:
            mid = (left+right)//2
            if A[mid] > target:
                right = mid
            elif  A[mid] < target:
                left = mid
            else:
                left = mid
                
        if A[right] == target:
            return right
        elif A[left] == target:
            return left
        else:
            return None
