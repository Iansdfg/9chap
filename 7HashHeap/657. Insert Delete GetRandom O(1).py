from random import randrange

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.pos = dict()
        self.nums = list()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        self.nums.append(val)
        self.pos[val] = len(self.nums)-1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.pos:
            return False
        
        val_index = self.pos[val] 
        last_ele = self.nums[-1]
        
        self.nums[val_index] = last_ele
        del self.pos[last_ele]
        self.pos[last_ele] = val_index
        
        self.nums.pop()
        return True
        
        
        

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        pos = randrange(len(self.nums))
        return self.nums[pos]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
