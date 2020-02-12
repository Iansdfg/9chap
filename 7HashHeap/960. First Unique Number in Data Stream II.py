class linkedNode:
    def __init__(self, val = None, key = None, next = None):
        # do intialization if necessar
        self.val = val
        self.key = key
        self.next = next
        
class DataStream:
    def __init__(self):
        # do intialization if necessary
        self.key_to_prev = dict()
        self.dummy = linkedNode(0)
        self.tail = self.dummy
        self.visited = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num in self.visited:
            return
        
        if num in self.key_to_prev:
            self.kick(num)
            self.visited.add(num)
        else:
            self.tail.next = linkedNode(num)
            self.key_to_prev[num] = self.tail
            self.tail = self.tail.next
            
                
    def kick(self,key):
        prev = self.key_to_prev[key]
        node = prev.next
        nextt = node.next
        
        prev.next = nextt
        node.next = None
        if nextt:
            self.key_to_prev[nextt.val] = prev
        else:
            self.tail = prev
        del self.key_to_prev[node.val]


    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        if self.dummy.next:
            return self.dummy.next.val
        else:
            return -1 
        
