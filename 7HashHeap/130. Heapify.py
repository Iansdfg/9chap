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

            
            
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for index in range(len(A)-1, -1, -1):
            self.siftup(A, index)
            
            
    def siftup(self, A, index):
        while index * 2 + 1 < len(A):
            left_child = index * 2 + 1
            right_child = index * 2 + 2 
            mini_index = index
            if left_child < len(A) and A[left_child] < A[mini_index]:
                mini_index = left_child
            if right_child < len(A) and A[right_child] < A[mini_index]:
                mini_index = right_child
                
            if mini_index == index:
                break 
            
            A[index], A[mini_index] = A[mini_index], A[index]
            index = mini_index
            
            
            
            
            
