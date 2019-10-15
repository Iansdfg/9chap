class CircularQueue:
    def __init__(self, n):
        # do intialization if necessary
        self.array = [0]*n
        self.size = 0
        self.front = 0
        self.rear = 0
    """
    @return:  return true if the array is full
    """
    def isFull(self):
        # write your code here
        return self.size == len(self.array)

    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):
        # write your code here
        return self.size == 0

    """
    @param element: the element given to be added
    @return: nothing
    """
    def enqueue(self, element):
        # write your code here
        self.rear = (self.front+ self.size)%len(self.array)
        self.array[self.rear] = element
        self.size+=1
        
    """
    @return: pop an element from the queue
    """
    def dequeue(self):
        # write your code here
        ele = self.array[self.front]
        self.front = (self.front + 1)%len(self.array)
        self.size-=1
        return ele 
