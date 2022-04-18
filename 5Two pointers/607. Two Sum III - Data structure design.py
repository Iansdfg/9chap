class TwoSum:
    num_freq= dict()
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number not in self.num_freq:
            self.num_freq[number] = 0
        self.num_freq[number] += 1
        
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.num_freq:
            self.num_freq[num] -= 1 
            if value - num in self.num_freq and self.num_freq[value - num]!=0:
                return True 
            self.num_freq[num] += 1
        return False 
