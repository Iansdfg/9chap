class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for order in range(len(A)):
            self.siftup(A, order)
            
            
    def siftup(self, A, order):
        while order:
            father_order = (order - 1) // 2
            if A[order] > A[father_order]:
                break
            A[order], A[father_order] = A[father_order], A[order]
            order = father_order
