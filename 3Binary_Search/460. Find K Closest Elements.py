class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        right = self.find_first_k(A, target)
        print(right)
        left = right-1
        nearKth = []
 
        for _ in range(k):
            if self.is_left_clother(A, target, left, right):
                nearKth.append(A[left])
                left-=1
            else:
                nearKth.append(A[right])
                right+=1
            
        return nearKth
 
    def find_first_k(self, A, target):
        start, end  = 0, len(A)-1
        while start+1<end:
            m = (start + end) // 2
            
            if A[m] < target:
                start = m
            elif A[m] > target:
                end = m
            else:
                return m
        
        return start if abs(A[start]-target) < abs(A[end]-target) else end
        
    def is_left_clother(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
