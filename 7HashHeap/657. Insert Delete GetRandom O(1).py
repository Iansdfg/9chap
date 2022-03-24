import random

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.nums = []
        self.num_to_pos = dict()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.num_to_pos:
            return False
        self.nums.append(val)
        self.num_to_pos[val] = len(self.nums)-1


    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.num_to_pos:
            return False

        pos = self.num_to_pos[val]
        last = self.nums[-1]

        self.nums[pos] = last
        self.num_to_pos[last] = pos 

        self.nums.pop()
        del self.num_to_pos[val]


    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.nums[random.randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
