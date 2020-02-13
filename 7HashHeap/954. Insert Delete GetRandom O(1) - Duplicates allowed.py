from collections import defaultdict
import random 
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.val_to_pos_list = defaultdict(set)
        
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.stack.append(val)
        self.val_to_pos_list[val].add(len(self.stack) - 1)
        return len(self.val_to_pos_list[val]) == 1
          
    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        # pop() for set is pop random
        if not self.val_to_pos_list[val]:
            return
        pos = self.val_to_pos_list[val].pop()
        self.stack[pos] = None 
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        ans = None 
        while not ans:
            ans = random.choice(self.stack)
        return ans


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
