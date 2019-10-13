class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A)//2, -1, -1):
            self.siftdown(A, i)
    
    
    def siftdown(self, Array, index):
        lenth = len(Array)
        mini_index = index 
        while index<lenth:
            left, right = index*2+1, index*2+2
            if left<lenth and Array[mini_index]>Array[left]:
                mini_index = left
            if right<lenth and Array[mini_index]>Array[right]:
                mini_index = right

            if mini_index == index:
                break
            
            Array[mini_index], Array[index] = Array[index], Array[mini_index]
            
            index = mini_index
