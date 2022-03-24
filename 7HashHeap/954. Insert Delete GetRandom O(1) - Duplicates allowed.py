from collections import defaultdict
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.num2indexList = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        if val in self.num2indexList:
            self.num2indexList[val].append(len(self.nums) - 1)
            return False
        else:
            self.num2indexList[val] = [len(self.nums) - 1]
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.num2indexList:
            index_list = self.num2indexList[val]
            last_pos = index_list.pop()
            if not index_list:
                del self.num2indexList[val]
            if last_pos != len(self.nums) - 1:
                last_num = self.nums[-1]
                self.num2indexList[last_num][-1] = last_pos
                self.nums[last_pos], self.nums[-1] = self.nums[-1], self.nums[last_pos]
            self.nums.pop()
            return True 
        else:
            return False 
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return random.choice(self.nums)
        
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
