class LinkedNode:

    def __init__(self, value=None, next=None):
        # do intialization if necessary
        self.value = value
        self.next = next

class DataStream:
    
    def __init__(self):
        # do intialization if necessary
        self.val_to_prev = dict()
        self.dummy = LinkedNode(-1)
        self.tail = self.dummy

    def kick(self, prev):
        if prev == self.tail:
            return
        node = prev.next
        next = node.next
        if not next:
            prev.next = None 
            self.tail = prev
            return
        prev.next = next
        self.val_to_prev[next.value] = prev
        self.val_to_prev[node.value] = None
        
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num not in self.val_to_prev:
            node = LinkedNode(num)
            self.tail.next = node
            self.val_to_prev[num] = self.tail
            self.tail = node
        else:
            if self.val_to_prev[num] == None:
                return
            prev = self.val_to_prev[num]
            self.kick(prev)

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        if self.dummy.next:
            return self.dummy.next.value
        else:
            return -1
