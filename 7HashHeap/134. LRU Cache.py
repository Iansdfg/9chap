class LinkedNode:
    
    def __init__(self, val = None, key = None, next=None):
        self.val = val
        self.key = key
        self.next = next
        
    # do intialization if necessary
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev = dict()
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy
        
        
    # prev--node--next--...---tail
    # prev--next--...---tail--node
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next:
            self.key_to_prev[node.next.key] = prev
            node.next = None
        self.append(node)
    
    def append(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
        
    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        
        
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.val
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.val = value
        else:
            self.append(LinkedNode(value, key))
            if self.capacity < len(self.key_to_prev):
                self.pop_front()
           
