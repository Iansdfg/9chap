from collections import deque
class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])
        
    def push(self, x):
        # write your code here
        self.queue1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.popleft() if len(self.queue2) != 0 else None

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.popleft())

        top = self.queue1[-1]
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top


    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.queue1) == 0 
