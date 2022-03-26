class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        # 从 n//2 位开始
        for index in range(len(A)//2, -1, -1):
            self.siftdown(A, index)
            
    def siftdown(self, A, index):
        # 如果在长度内
        while index < len(A):
            left_child = index * 2 + 1
            right_child = index * 2 + 2 
            mini_index = index
            # 如果左子小，左子的index为最小
            if left_child < len(A) and A[left_child] < A[mini_index]:
                mini_index = left_child
            # 如果右子小，右子的index为最小
            if right_child < len(A) and A[right_child] < A[mini_index]:
                mini_index = right_child
            # 如果父节点最小 进入下一轮
            if mini_index == index:
                break 

            A[index], A[mini_index] = A[mini_index], A[index]
            
            index = mini_index
            
            
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A) // 2, -1, -1):
            self.sift_down(A, i)


    def sift_down(self, A, index):
        length = len(A)
        while index < length:
            left = 2 * index + 1 
            right = 2 * index + 2
            minindex = index
            if left < length and A[left] < A[minindex]:
                minindex = left
            if right < length and A[right] < A[minindex]:
                minindex = right

            if index == minindex:
                break
            A[index], A[minindex] = A[minindex], A[index]
            index = minindex
            
            
