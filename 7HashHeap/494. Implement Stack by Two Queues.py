from collections import deque

class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    def move(self):
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.popleft())
        
    def switch(self):
        self.queue1, self.queue2 = self.queue2, self.queue1
    
    def push(self, x):
        # write your code here
        self.queue1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.move()
        self.switch()
        self.queue2.popleft()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        self.move()
        ans = self.queue1.popleft()
        self.queue2.append(ans)
        self.switch()
        return ans

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.queue1) == 0
