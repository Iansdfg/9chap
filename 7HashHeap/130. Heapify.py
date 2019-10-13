class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        for i in range(len(A)//2, -1, -1):
            self.siftdown(A, i)
            
    def siftdown(self, A, index):
        n = len(A)
        while index<n:
            left = index*2+1
            right = index*2+2
            mini_index = index
            if left<n and A[mini_index]>A[left]:
                mini_index = left
                
            if right<n and A[mini_index]>A[right]:
                mini_index = right
                
            if mini_index == index:
                break
            
            A[mini_index], A[index] = A[index], A[mini_index]
            
            index = mini_index
                
                
                
