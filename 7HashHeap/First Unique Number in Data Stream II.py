class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class DataStream:
    def __init__(self):
        # do intialization if necessary
        self.dummy = LinkedNode(-1)
        self.tail = self.dummy 
        self.num_to_prev = dict()
        self.dupulicated = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num in self.dupulicated:
            return
        
        if num not in self.num_to_prev:
            self.push_back(num)
            return
        
        self.dupulicated.add(num)
        self.remove(num)
            
            
    def remove(self, num):
        prev = self.num_to_prev[num]
        del self.num_to_prev[num]
        
        prev.next = prev.next.next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev
        
    
    def push_back(self, num):
        node = LinkedNode(num)
        self.tail.next = node
        self.num_to_prev[num] = self.tail
        self.tail = node
        

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        if not self.dummy.next:
            return None
        return self.dummy.next.val
        
