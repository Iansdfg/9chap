from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = deque()
        self.size = size
        self.summ = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.queue.append(val)
        self.summ += val
        if len(self.queue) > self.size:
            sub = self.queue.popleft()
            self.summ -= sub
        return self.summ/len(self.queue)
            
        
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
