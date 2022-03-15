class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.num_to_cnt = {}

    def add(self, number):
        # write your code here
        if number in self.num_to_cnt:
            self.num_to_cnt[number] += 1
        else:
            self.num_to_cnt[number] = 1 

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.num_to_cnt:
            if value - num != num and value - num in self.num_to_cnt :
                return True 
            if value - num == num and self.num_to_cnt[num] > 1:
                return True 
        return False 
