class TwoSum:
    def __init__(self):
        self.count = dict()
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number not in self.count:
            self.count[number] = 1
        else: 
            self.count[number] += 1
            

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.count:
            if value-num != num and value-num in self.count:
                return True
            if value-num == num and self.count[num]>1:
                return True
        return False
