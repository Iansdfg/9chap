class LinkedNode:
    def __init__(self, key=None, value=None, next_node=None):
        # do intialization if necessary
        self.key = key
        self.value = value
        self.next_node = next_node

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        #we need to delete, so key to prev
        self.key_to_prev = dict()
        self.dummy = LinkedNode(-1)
        self.tail = self.dummy

    def kick_append(self, prev):
        #prev-->curr-->next->..->tail
        #prev-->next->..->tail-->curr
        curr = prev.next_node
        if curr == self.tail:
            return
        nextt = curr.next_node

        prev.next_node = nextt
        self.key_to_prev[nextt.key] = prev
        curr.next_node = None

        self.append(curr)

    def append(self, node):
        self.tail.next_node = node
        self.key_to_prev[node.key] = self.tail
        self.tail = node

    def kick_front(self):
        head = self.dummy.next_node
        nextt = head.next_node
        self.dummy.next_node = nextt
        self.key_to_prev[nextt.key] = self.dummy
        head.next_node = None
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
        curr = prev.next_node

        self.kick_append(prev)

        return curr.value 

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            prev = self.key_to_prev[key]
            curr = prev.next_node
            curr.value = value
            self.kick_append(prev)
        else:
            node = LinkedNode(key, value)
            self.append(node)
            if len(self.key_to_prev) > self.capacity:
                self.kick_front()

        
            

