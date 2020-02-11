class LinkedNode:
    def __init__(self, val = None, key = None, next = None):
        self.val = val
        self.key = key
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev = dict()
        self.capacity = capacity
        self.dummy = LinkedNode(0)
        self.tail = self.dummy
        
    # prev--node--next---...--tail
    # prev--next---...--tail--node
    def kick_append(self, prev):
        node = prev.next 
        if node == self.tail:
            return
        nextt = node.next
        prev.next = nextt
        
        if nextt:
            self.key_to_prev[nextt.key] = prev
            node.next = None 
        self.append(node)

    def append(self, node):
        self.tail.next = node 
        self.key_to_prev[node.key] = self.tail
        self.tail = node
        
    def pop_front(self,):
        head = self.dummy.next
        nextt = head.next 
        self.key_to_prev[nextt.key] = self.dummy
        self.dummy.next = nextt
        head.next = None 
        del self.key_to_prev[head.key]
        
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1 
        
        prev = self.key_to_prev[key]
        node = prev.next
        
        self.kick_append(prev)
        
        return node.val
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            prev = self.key_to_prev[key]
            node = prev.next 
            node.val = value
            
            self.kick_append(prev)
            
        else:
            node = LinkedNode(value, key)
            self.append(node)
            if len(self.key_to_prev) > self.capacity:
                self.pop_front()
                
  
