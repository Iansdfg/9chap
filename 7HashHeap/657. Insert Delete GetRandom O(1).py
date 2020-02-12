import random
class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.val_to_pos = dict()
        self.stack = []

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.stack:
            return
        self.stack.append(val)
        self.val_to_pos[val] =  len(self.stack) - 1
        
    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.stack:
            return
        
        pos = self.val_to_pos[val]
        last_val = self.stack[-1]
        
        self.stack[pos] = last_val
        self.val_to_pos[last_val] = pos
        
        self.stack.pop()
        del self.val_to_pos[val]
        

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        pos = random.randint(0, len(self.stack) - 1)
        return self.stack[pos]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
